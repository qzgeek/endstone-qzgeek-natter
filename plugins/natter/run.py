import subprocess
import time
import os
import sys
from datetime import datetime

def run_and_monitor():
    command = [
        'python3', 
        'natter.py', 
        '-p', '19132', ### 这里改成你服务器配置文件里设置的端口号（说白了就是本地端口号）
        '-u', 
        '-e', 'output.py',
        '-q'
    ]
    
    while True:
        try:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 启动进程: {' '.join(command)}")
            
            # 启动子进程，捕获标准输出和错误输出
            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1  # 行缓冲，实时输出
            )
            
            # 实时读取并显示输出
            for line in process.stdout:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] {line.strip()}")
            
            # 等待进程退出
            process.wait()
            exit_code = process.returncode
            
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 进程退出，退出码: {exit_code}")
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 正在重启...")
            
        except Exception as e:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 发生错误: {str(e)}")
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 正在重启...")
        
        # 重启前等待2秒，避免频繁重启
        time.sleep(2)

if __name__ == "__main__":
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 监控程序启动，目标进程: {'python3 /root/natter/natter.py -p 19133 -u -e output.py'}")
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 按Ctrl+C停止监控")
    
    try:
        run_and_monitor()
    except KeyboardInterrupt:
        print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 用户中断，程序退出")
        sys.exit(0)
