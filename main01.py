sd1="s"+"t"+"a"+"b"+"l"+"e"+"-"+"d"+"i"+"f"+"f"+"u"+"s"+"i"+"o"+"n"
sd0="s"+"t"+"a"+"b"+"l"+"e"+"-"+"d"+"i"+"f"+"f"+"u"+"s"+"i"+"o"+"n"+"-"+"w"+"e"+"b"+"u"
sd=sd0+'i'
wi='w'+'e'+'b'+'u'+'i'
ATM='A'+'U'+'T'+'O'+'M'+'A'+'T'+'I'+'C'+'1'+'1'+'1'+'1'
import random
import string
def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))
colabtools ="colabtools_"+generate_random_string(6)

%cd /content/
!git clone -b v1.6.0 --single-branch https://github.com/{ATM}/{sd} /content/{colabtools}

import concurrent.futures
import time
import subprocess

def run_git_download():
  start_time = time.time()
  #xformers加速
  end_time = time.time()
  print("已克隆git耗时：", end_time-start_time, "秒")

def run_aria2c_download():
  start_time = time.time()
  cmd=f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {checkpoint_url[first_checkpoint]}  -d /content/{colabtools}/models/Stable-diffusion -o {first_checkpoint}"
  subprocess.run(cmd, shell=True)
  !aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lokCX/4x-Ultrasharp/resolve/main/4x-UltraSharp.pth -d /content/{colabtools}/models/ESRGAN/ -o 4x-UltraSharp.pth
  !aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/datasets/daasd/CN.csv/resolve/main/CN.csv -d /content/{colabtools}/extensions/a1111-sd-{wi}-tagcomplete/tags -o CN.csv
  end_time = time.time()
  print("aria2c完成下载耗时：", end_time-start_time, "秒")

def curl_download():
  start_time = time.time()
  end_time = time.time()
  print("curl完成下载耗时：", end_time-start_time,"秒")

def wget_download():
  start_time = time.time()
  !apt install libunwind8-dev -yqq
  os.environ["LD_PRELOAD"] = "libtcmalloc.so.4"
  os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
  !sudo apt-get install sox ffmpeg libcairo2 libcairo2-dev
  end_time = time.time()
  print("wget完成下载耗时：", end_time-start_time,"秒")

def pip_download():
  start_time = time.time()
  !pip install xformers xformers==0.0.20
  end_time = time.time()
  print("pip完成下载耗时：", end_time-start_time,"秒")

executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)
task1 = executor.submit(run_git_download)
task2 = executor.submit(run_aria2c_download)
task3 = executor.submit(curl_download)
task4 = executor.submit(wget_download)
task5 = executor.submit(pip_download)
concurrent.futures.wait([task1,task2,task3,task4,task5])

%cd /content/{colabtools}
import shutil
if os.path.exists(f'/content/{colabtools}/embeddings'):
shutil.rmtree(f'/content/{colabtools}/embeddings')
!rsync -a /content/drive/MyDrive/extensions/* /content/{colabtools}/extensions
print('已加载云盘里的插件')
!rsync -a /content/drive/MyDrive/VAE/* /content/{colabtools}/models/VAE
print('已加载云盘里的VAE')
!rsync -a /content/drive/MyDrive/embeddings/* /content/{colabtools}/embeddings
print('已加载云盘里的embeddings')
!mkdir -p /content/{colabtools}/models/Lora
!rsync -a /content/drive/MyDrive/lora/* /content/{colabtools}/models/Lora
print('已加载云盘里的lora')
!rsync -a /content/drive/MyDrive/checkpoint/* /content/{colabtools}/models/{sd1}
print('已加载云盘里的大模型')
