import concurrent.futures
import time
import subprocess
import random
import string
import os

# 指定要进入的文件夹路径
folder_path = "/content/drive/MyDrive/SB"
# 使用os.chdir()进入文件夹
os.chdir(folder_path)

command01 = "apt rm -rf /content/drive/MyDrive/SB/repositories/CodeFormer"
subprocess.run(command01, shell=True)

command02 = "apt git clone https://github.com/sczhou/CodeFormer /content/drive/MyDrive/SB/repositories/CodeFormer"
subprocess.run(command02, shell=True)

command03 = command03 = "git -C \"/content/drive/MyDrive/SB/repositories/CodeFormer\" checkout --force 8392d0334956108ab53d9439c4b9fc9c4af0d66d"
subprocess.run(command03, shell=True)

# 用您的系统命令替换下面的内容
system_command = "python launch.py --share --lowram  --disable-safe-unpickle --disable-console-progressbars --xformers --enable-insecure-extension-access  --opt-sub-quad-attention --opt-channelslast --api --theme dark"

# 使用subprocess执行命令
subprocess.run(system_command, shell=True)
