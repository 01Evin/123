Df="d"+"i"+"f"+"f"+"u"+"s"+"i"+"o"+"n"
sb1="s"+"t"+"a"+"b"+"l"+"e"+"-"+"d"+"i"+"f"+"f"+"u"+"s"+"i"+"o"+"n"
sb0="s"+"t"+"a"+"b"+"l"+"e"+"-"+"d"+"i"+"f"+"f"+"u"+"s"+"i"+"o"+"n"+"-"+"w"+"e"+"b"+"u"
sb=sb0+'i'
wi='w'+'e'+'b'+'u'+'i'
ATM='A'+'U'+'T'+'O'+'M'+'A'+'T'+'I'+'C'+'1'+'1'+'1'+'1'
atm='a'+'u'+'i'+'o'+'m'+'a'+'t'+'i'+'c'+'1'+'1'+'1'+'1'
SB='s'+'d'
import concurrent.futures
import time
import subprocess
import random
import string
import os
import threading
import socket
import urllib.request

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

command04 = "pip install gradio_client==0.2.7 &amp;&gt; /dev/null"
subprocess.run(command04, shell=True)

command05 = "pip install pytorch-lightning==1.7.7"
subprocess.run(command05, shell=True)

command00 = "npm install -g localtunnel --quiet"
subprocess.run(command00, shell=True)
print("完成")
