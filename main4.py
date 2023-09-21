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

command01 = "rm -rf /content/drive/MyDrive/SB/repositories/CodeFormer"
subprocess.run(command01, shell=True)

command02 = "git clone https://github.com/sczhou/CodeFormer /content/drive/MyDrive/SB/repositories/CodeFormer"
subprocess.run(command02, shell=True)

command03 = "git -C \"/content/drive/MyDrive/SB/repositories/CodeFormer\" checkout --force c5b4593074ba6214284d6acd5f1719b6c5d739af"
subprocess.run(command03, shell=True)

command04 = "pip install gradio_client==0.2.7"
subprocess.run(command04, shell=True)

command05 = "pip install pytorch-lightning==1.7.7"
subprocess.run(command05, shell=True)

# 用您的系统命令替换下面的内容
system_command = "python launch.py --share --lowram  --disable-safe-unpickle --disable-console-progressbars --xformers --enable-insecure-extension-access  --opt-sub-quad-attention --opt-channelslast --api --theme dark"

# 使用subprocess执行命令
subprocess.run(system_command, shell=True)
