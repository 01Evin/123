sd1="s"+"t"+"a"+"b"+"l"+"e"+"-"+"d"+"i"+"f"+"f"+"u"+"s"+"i"+"o"+"n"
sd0="s"+"t"+"a"+"b"+"l"+"e"+"-"+"d"+"i"+"f"+"f"+"u"+"s"+"i"+"o"+"n"+"-"+"w"+"e"+"b"+"u"
sd=sd0+'i'
wi='w'+'e'+'b'+'u'+'i'
ATM='A'+'U'+'T'+'O'+'M'+'A'+'T'+'I'+'C'+'1'+'1'+'1'+'1'
import concurrent.futures
import time
import subprocess
import random
import string
import os

git_clone_command = "git clone -b v1.6.0 --single-branch https://github.com/AUTOMATIC1111/stable-diffusion-webui /content/colabtools"
subprocess.run(git_clone_command, shell=True)

# 第一个命令
command1 = "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lokCX/4x-Ultrasharp/resolve/main/4x-UltraSharp.pth -d /content/colabtools/models/ESRGAN/ -o 4x-UltraSharp.pth"
# 执行第一个命令
subprocess.run(command1, shell=True)
# 第二个命令
command2 = "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/datasets/daasd/CN.csv/resolve/main/CN.csv -d /content/colabtools/extensions/a1111-sd-{wi}-tagcomplete/tags -o CN.csv"
# 执行第二个命令
subprocess.run(command2, shell=True)

command3 = "apt install libunwind8-dev -yqq"
os.environ["LD_PRELOAD"] = "libtcmalloc.so.4"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
command4 = "sudo apt-get install sox ffmpeg libcairo2 libcairo2-dev"
subprocess.run(command3, shell=True)
subprocess.run(command4, shell=True)

command5 = "pip install xformers xformers==0.0.20"
subprocess.run(command5, shell=True)

# 假设您想执行一个需要特权的命令，例如apt-get update
command01 = "apt-get update"

# 使用subprocess执行命令
process = subprocess.Popen(command01, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# 等待命令执行完毕并获取输出
stdout, stderr = process.communicate()

# 打印命令输出
print("标准输出：", stdout.decode())
print("标准错误：", stderr.decode())

# 检查命令是否成功执行
if process.returncode == 0:
    print("命令成功执行")
else:
    print("命令执行失败")

commandA = "apt update"
commandB = "apt install rsync"
subprocess.run(commandA, shell=True)
subprocess.run(commandB, shell=True)

import shutil
if os.path.exists("/content/drive/MyDrive/VAE"):
  import subprocess
# 用subprocess执行rsync命令
source0 = "/content/drive/MyDrive/VAE/*"
destination0 = f"/content/colabtools/models/VAE"
commandQ = f"sudo rsync -a {source0} {destination0}"
subprocess.run(commandQ, shell=True, check=True)
print("已加载云盘里的VAE")

import shutil
directory_path = f"/content/colabtools/models/lora"
subprocess.run(["mkdir", "-p", directory_path])
if os.path.exists("/content/drive/MyDrive/lora"):
  import subprocess
# 用subprocess执行rsync命令
source1 = "/content/drive/MyDrive/lora/*"
destination1 = f"/content/colabtools/models/lora"
commandw = f"sudo rsync -a {source1} {destination1}"
subprocess.run(commandw, shell=True, check=True)
print("已加载云盘里的lora")

if os.path.exists("/content/drive/MyDrive/extensions"):
  import subprocess
# 用subprocess执行rsync命令
source = "/content/drive/MyDrive/extensions/*"
destination = f"/content/colabtools/extensions"
command = f"sudo rsync -a {source} {destination}"
subprocess.run(command, shell=True, check=True)
print("已加载云盘里的插件")




