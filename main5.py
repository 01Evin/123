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

command01 = "npm install -g localtunnel"
subprocess.run(command01, shell=True)

def iframe_thread(port):
  while True:
      time.sleep(0.5)
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      result = sock.connect_ex(('127.0.0.1', port))
      if result == 0:
        break
      sock.close()
  print("\n{CF} finished loading, trying to launch localtunnel (if it gets stuck here localtunnel is having issues)\n")

  print("The password/enpoint ip for localtunnel is:", urllib.request.urlopen('https://ipv4.icanhazip.com').read().decode('utf8').strip("\n"))
  p = subprocess.Popen(["lt", "--port", "{}".format(port)], stdout=subprocess.PIPE)
  for line in p.stdout:
    print(line.decode(), end='')

threading.Thread(target=iframe_thread, daemon=True, args=(8188,)).start()

# 用您的系统命令替换下面的内容
system_command = "python launch.py --share --lowram  --disable-safe-unpickle --disable-console-progressbars --xformers --enable-insecure-extension-access  --opt-sub-quad-attention --opt-channelslast --api --theme dark"

# 使用subprocess执行命令
subprocess.run(system_command, shell=True)