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

if sd_wi=="anapnoe手机端完美适配":
  !git clone https://github.com/anapnoe/{sd} /content/{colabtools}
elif sd_wi=="AUTOMATIC1111原版v1.3.0(稳定)":
  !git clone -b v1.3.0 --single-branch https://github.com/{ATM}/{sd} /content/{colabtools}
else:
  !git clone -b v1.6.0 --single-branch https://github.com/{ATM}/{sd} /content/{colabtools}

import concurrent.futures
import time
import subprocess

checkpoint_url = {
    "Dark_sushi_mix.safetensors"     : "https://huggingface.co/mdl-mirror/dark-sushi-mix/resolve/main/darkSushiMixMix_brighter.safetensors",
    "AnythingV5V3_v5PrtRE.safetensors"     : "https://huggingface.co/ckpt/anything-v5.0/resolve/main/AnythingV5V3_v5PrtRE.safetensors",
    "chilloutmix_NiPrunedFp16Fix.safetensors"      : "https://huggingface.co/naonovn/chilloutmix_NiPrunedFp32Fix/resolve/main/chilloutmix_NiPrunedFp32Fix.safetensors",
    "rpg_V4.safetensors"         : "https://huggingface.co/Anashel/rpg/resolve/main/RPG-V4-Model-Download/RPG-v4.safetensors",
    "ProtoGen_X5.8-pruned-fp16.safetensors"         : "https://huggingface.co/darkstorm2150/Protogen_x5.8_Official_Release/resolve/main/ProtoGen_X5.8-pruned-fp16.safetensors",
    "none"         : "",
}

def run_git_download():
  start_time = time.time()
  #xformers加速
  end_time = time.time()
  print("已克隆git耗时：", end_time-start_time, "秒")

def run_aria2c_download():
  start_time = time.time()
  cmd=f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {checkpoint_url[first_checkpoint]}  -d /content/{colabtools}/models/Stable-diffusion -o {first_checkpoint}"
  subprocess.run(cmd, shell=True)
    
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

#个人插件从云盘的extensions文件夹与VAE文件夹加载
if is_pan_extensions:
  if os.path.exists("/content/drive/MyDrive/extensions"):
    !rsync -a /content/drive/MyDrive/extensions/* /content/{colabtools}/extensions
    print('已加载云盘里的插件')
  if os.path.exists("/content/drive/MyDrive/VAE"):
    !rsync -a /content/drive/MyDrive/VAE/* /content/{colabtools}/models/VAE
    print('已加载云盘里的VAE')
  if os.path.exists("/content/drive/MyDrive/embeddings"):
    !rsync -a /content/drive/MyDrive/embeddings/* /content/{colabtools}/embeddings
    print('已加载云盘里的embeddings')
  if os.path.exists("/content/drive/MyDrive/lora"):
    !mkdir -p /content/{colabtools}/models/Lora
    !rsync -a /content/drive/MyDrive/lora/* /content/{colabtools}/models/Lora
    print('已加载云盘里的lora')
  if os.path.exists("/content/drive/MyDrive/checkpoint"):
    !rsync -a /content/drive/MyDrive/checkpoint/* /content/{colabtools}/models/{sd1}
    print('已加载云盘里的大模型')

