#!/usr/bin/env python3

import sys
import os
import json

# Natter notification script arguments
protocol, private_ip, private_port, public_ip, public_port = sys.argv[1:6]

print(public_ip + ':' + public_port)

# 生成host.json文件
host_data = {
    "host": public_ip,
    "port": public_port
}

# 写入JSON文件到运行目录
with open("host.json", "w") as f:
    json.dump(host_data, f, indent=4)
