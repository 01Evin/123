import concurrent.futures
import time
import subprocess
import random
import string
import os

git_clone_command = "git clone -b v1.6.0 --single-branch https://github.com/AUTOMATIC1111/stable-diffusion-webui /content/drive/MyDrive/SB"
subprocess.run(git_clone_command, shell=True)

# 第一个命令
command1 = "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lokCX/4x-Ultrasharp/resolve/main/4x-UltraSharp.pth -d /content/drive/MyDrive/SB/models/ESRGAN/ -o 4x-UltraSharp.pth"
# 执行第一个命令
subprocess.run(command1, shell=True)
# 第二个命令

command3 = "apt install libunwind8-dev -yqq"
os.environ["LD_PRELOAD"] = "libtcmalloc.so.4"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
command4 = "sudo apt-get install sox ffmpeg libcairo2 libcairo2-dev"
subprocess.run(command3, shell=True)
subprocess.run(command4, shell=True)

command4 = "pip install -q torch==2.0.0+cu118 torchvision==0.15.1+cu118 torchaudio==2.0.1+cu118 torchtext==0.15.1 torchdata==0.6.0 --extra-index-url https://download.pytorch.org/whl/cu118 -U"
subprocess.run(command4, shell=True)

command5 = "pip install xformers xformers==0.0.20"
subprocess.run(command5, shell=True)
print("Done!")
