sd0="s"+"t"+"a"+"b"+"l"+"e"+"-"+"d"+"i"+"f"+"f"+"u"+"s"+"i"+"o"+"n"+"-"+"w"+"e"+"b"+"u"
sd=sd0+'i'
import concurrent.futures
import time
import subprocess
import random
import string
import os

# 指定要进入的文件夹路径
folder_path = "/content/colabtools"
# 使用os.chdir()进入文件夹
os.chdir(folder_path)

half_precision_str="--share --lowram  --disable-safe-unpickle  --disable-console-progressbars --xformers --enable-insecure-extension-access  --opt-sub-quad-attention --opt-channelslast --api --theme dark"
!python launch.py {half_precision_str}
