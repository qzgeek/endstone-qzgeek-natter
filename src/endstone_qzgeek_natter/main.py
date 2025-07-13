from endstone.plugin import Plugin
from endstone.command import Command, CommandSender
from endstone import ColorFormat, Player
from endstone.form import ActionForm
from endstone.event import event_handler, PlayerJoinEvent
import os
import json
import time
from endstone.scheduler import Task

# 获取当前插件的运行目录
current_dir = os.getcwd()
first_dir = os.path.join(current_dir, 'plugins', 'natter')

if not os.path.exists(first_dir):
    os.mkdir(first_dir)
    
host_file_path = os.path.join(first_dir, 'host.json')

class NatterMain(Plugin):
    api_version = "0.5"
    
    def __init__(self):
        super().__init__()
        # 初始化host和port变量
        self.host = ""
        self.port = 0
        # 记录上次读取时间
        self.last_read_time = 0
        # 启动定时任务
        self.refresh_task = None
        # 记录玩家上次显示提示的时间（时间戳）
        self.last_prompt_times = {}
        # 提示间隔时间（秒）
        self.prompt_interval = 60  # 1分钟

    def on_enable(self) -> None:
        self.logger.info(f"{ColorFormat.YELLOW}Natter插件已启用，正在监听host.json...")
        # 首次读取host.json
        self.read_host_config()
        # 启动30秒刷新任务
        self.refresh_task = self.server.scheduler.run_task(
            self, self.refresh_host_config, delay=0, period=30
        )
        # 注册事件监听
        self.register_events(self)

    def on_disable(self) -> None:
        # 插件禁用时取消定时任务
        if self.refresh_task:
            self.server.scheduler.cancel_task(self.refresh_task.task_id)

    commands = {
        "natter": {
            "description": "切换线路",
            "usages": ["/natter"],
            "permissions": ["qzgeek_natter.command.natter"],
        }
    }

    permissions = {
        "qzgeek_natter.command.natter": {
            "description": "§b§l§o切换线路",
            "default": True,
        }
    }
    
    def on_command(self, sender: CommandSender, command: Command, args: list[str]) -> bool:
        if not isinstance(sender, Player):
            self.logger.error(f"{ColorFormat.RED}该命令只能由玩家执行")
            return True
            
        if command.name == "natter":
            player = self.server.get_player(sender.name)
            if not player:
                return True
                
            try:
                # 使用当前host和port执行跳转
                player.transfer(str(self.host), int(self.port))
                self.logger.info(f"{ColorFormat.GREEN}玩家 {sender.name} 已切换至 {self.host}:{self.port}")
            except Exception as e:
                self.logger.error(f"{ColorFormat.RED}切换线路失败: {str(e)}")
                player.send_message(f"{ColorFormat.RED}切换线路失败，请检查配置文件")
        return True

    def read_host_config(self):
        # 读取host.json以获取natter打洞的外网IP和端口
        try:
            if os.path.exists(host_file_path):
                with open(host_file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # 读取host和port
                    self.host = data.get("host", "")
                    self.port = data.get("port", 0)
                    self.last_read_time = time.time()
                    self.logger.info(f"{ColorFormat.YELLOW}成功读取host配置: {self.host}:{self.port}")
            else:
                self.logger.warning(f"{ColorFormat.YELLOW}host.json不存在，使用默认值")
        except Exception as e:
            self.logger.error(f"{ColorFormat.RED}读取host.json失败: {str(e)}")

    def refresh_host_config(self):
        # 定时刷新host配置，若文件修改则重新读取
        try:
            if os.path.exists(host_file_path):
                file_mod_time = os.path.getmtime(host_file_path)
                # 检查文件是否被修改（或达到30秒刷新周期）
                if file_mod_time > self.last_read_time:
                    self.read_host_config()
        except Exception as e:
            self.logger.error(f"{ColorFormat.RED}刷新host配置失败: {str(e)}")
    
    @event_handler
    def on_player_join(self, event: PlayerJoinEvent):
        # 玩家加入服务器时触发提示（1分钟内仅显示一次）
        player = event.player
        player_xuid = player.xuid
        current_time = time.time()
        
        # 检查上次显示时间是否在间隔内
        last_time = self.last_prompt_times.get(player_xuid, 0)
        if current_time - last_time < self.prompt_interval:
            return  # 1分钟内不重复显示
            
        # 创建询问表单
        form = ActionForm(
            title="§l§d直连线路切换",
            content="§a欢迎来到§l§e♂神♂奇♂§r§a的服务器，是否切换至直连线路？（直链更快，代理容易发生网络波动，且延迟较高）"
        )
        form.add_button(
            text="§l§a是 (切换线路)",
            on_click=lambda p: self.handle_switch(p)
        )
        # 玩家选“否”
        form.add_button(
            text="§l§c我已是直链 (不切换)",
            on_click=lambda p: p.send_message(f"{ColorFormat.GREEN}已取消切换，如需切换可使用命令 /natter")
        )
        
        # 发送表单并记录当前时间
        player.send_form(form)
        self.last_prompt_times[player_xuid] = current_time
    
    def handle_switch(self, player: Player):
        # 处理玩家选择“是”的情况，执行/natter命令
        # 直接调用命令逻辑
        self.server.dispatch_command(player, "natter")
