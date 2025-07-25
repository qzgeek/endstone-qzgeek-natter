![Natter](https://img.remit.ee/api/file/BQACAgUAAyEGAASHRsPbAAIxgmh0ZEnvGAT7cljyQ6VpQxzGIg17AAIOGAACeIOoV2ZGxYdD9pv-NgQ.png)
# ✨EndStone-QZGeek-Natter✨

让你的 Minecraft 服务器玩家 **丝滑直连**，告别穿透延迟！🚀 。

## 它能干嘛？ 🤔

1.  **自动抓取 & 守护 Natter** 🔄
    *   插件会自动获取你通过 `Natter` 打洞成功的外网 IP 和端口。
    *   时刻盯着 Natter，如果端口变了？**自动重启 Natter 并拿到新地址！** 省心！
    *   努力保持你的 Natter 进程稳定运行。

2.  **一键优化玩家连接** ⚡️
    *   玩家在游戏里输入 **`/natter`** 指令，就能瞬间切换到 Natter 的**直连 IP 和端口**。
    *   效果？延迟更低，带宽更足，游戏更流畅！玩家乐开花 😄

3.  **智能提醒不烦人** 📢
    *   玩家进服自动弹出窗口，提醒更换Natter线路。
    *   贴心防刷屏：**1分钟内**重进服务器不会弹出提醒，只有在服务器启动后首次进服或进服后1分钟后重新进服才会提醒（遇到切换线路后重新提醒的可以直接点否）

## 怎么安装？ 🛠️

1. **下载并解压压缩包**
2. **安装插件**
    *   将解压出的**插件本体**和**natter**目录复制到服务器**plugins**目录下
    （记得确保natter目录下的每个文件都有可执行权限）

## 怎么启动？ 🔛

*   首先找到服务器插件目录下**natter**目录下的**run.py**文件，打开并翻到第**11**行，将数字"19132"修改为你服务器本地的端口号，修改完成后保存
*   然后运行**run.py**，记得保证该程序一直在后台运行
*   最后启动服务器，观察到插件获取到Natter的外网IP和端口后就可以放心游戏了

## ❓亿些答疑❓

1. **什么是[Natter](https://github.com/MikeWang000000/Natter)啊？？**
    *   [Natter](https://github.com/MikeWang000000/Natter)是一个打洞工具，可以将你处于运营商内网的服务器端口打洞到外网供玩家访问。

2. **为什么我执行run.py后看到Natter在正常运行，服务器也获得了外网IP端口，但使用插件跳转（或是直接尝试连接该IP和端口）就是连接不上服务器呢？？**
    *   这说明你服务器所在的网络环境不符合要求。Natter需要全锥形网络（NAT1）才能成功打洞，如果你的服务器的网络环境不满足该要求，那么就无法使用该工具。

3. **我该怎么知道我的网络是不是全锥形网络（NAT1）呢？？**
    *   您可以先直接运行natter目录下的natter.py文件（python3 natter.py），看他的提示信息是不是像下面这样：

```
    2025-07-13 21:00:58 [I] LAN > 192.168.1.2:1145    [ OPEN ]
    2025-07-13 21:00:58 [I] LAN > 192.168.1.2:1145    [ OPEN ]
    2025-07-13 21:00:59 [I] LAN > 11.45.14.19:19810  [ OPEN ]
    2025-07-13 21:01:07 [I] WAN > 11.45.14.19:19810  [ OPEN ]
```
  *   如果是，那么恭喜你，您的网络完全符合要求！
  *   如果是像下面这样，那就说明您的网络不符合要求：
```
    2025-07-13 21:00:58 [I] LAN > 192.168.1.2:1145    [ OPEN ]
    2025-07-13 21:00:58 [I] LAN > 192.168.1.2:1145    [ OPEN ]
    2025-07-13 21:00:59 [I] LAN > 11.45.14.19:19810  [ CLOSED ]
    2025-07-13 21:01:07 [I] WAN > 11.45.14.19:19810  [ CLOSED ]
```

4. **我的网络不符合要求，是不是真的就没法使用Natter工具了？？**
    *   非也，你也可以尝试下面的方法优化网络类型，尽力将其提高到NAT1（⚠️注意⚠️：操作有风险，请谨慎操作，否则后果自负！）：
    *   https://help.onethingcloud.com/9dd6/7bab
    *   https://mao.fan/article/90
    *   https://www.bilibili.com/opus/1003608590061142054
    *   https://www.pcdndh.cn/article/changjianwenti/165.html
    *   如果整不了或者整了还是不行那还是老老实实用内网穿透吧，内网穿透也不是不行，是吧_(:зゝ∠)_

5. **主播主播，你这个插件也太简陋了，功能也太少了，太麻烦了吧，有没有什么既简单又强势的插件呢？？**
    *   没有的兄弟，没有，这插件才整出来，能用就不错了，添加功能啥的等我之后更新再说ᯠ  _   ̫  _ ̥ ᯄ ੭

6. **请问为什么我运行run.py后没看到Natter正常运行/Natter运行后没能正常带起output.py呢？？**
    *    检查natter目录下的三个文件（run.py、natter.py、output.py）是否都有可执行权限，没有就加上