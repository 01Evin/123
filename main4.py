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

# 用您的系统命令替换下面的内容
system_command = "python launch.py --share --lowram  --disable-safe-unpickle --disable-console-progressbars --xformers --enable-insecure-extension-access  --opt-sub-quad-attention --opt-channelslast --api --theme dark"

# 使用subprocess执行命令
subprocess.run(system_command, shell=True)
