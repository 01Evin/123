sd0="s"+"t"+"a"+"b"+"l"+"e"+"-"+"d"+"i"+"f"+"f"+"u"+"s"+"i"+"o"+"n"+"-"+"w"+"e"+"b"+"u"
sd=sd0+'i'
%cd /content/{colabtools}
#@markdown ####全精度/半精度(推荐)启动：##
is_full_precision = False  # @param {type:'boolean'}
#@markdown ####主题切换为暗配色：##
is_black = False  # @param {type:'boolean'}
#@markdown ####(可选)获取[ngrok](https://dashboard.ngrok.com/get-started/your-authtoken)的token进行免费网络加速：##
ngrok_auth=""  #@param {type:"string"}

full_precision_str="--share --lowram --disable-safe-unpickle  --disable-console-progressbars --xformers --enable-insecure-extension-access --precision full --no-half --no-half-vae --opt-sub-quad-attention --opt-channelslast --api"
half_precision_str="--share --lowram  --disable-safe-unpickle  --disable-console-progressbars --xformers --enable-insecure-extension-access  --opt-sub-quad-attention --opt-channelslast --api"
if is_black:
  full_precision_str+=" --theme='dark'"
  half_precision_str+=" --theme='dark'"
else:
  full_precision_str+=" --theme='light'"
  half_precision_str+=" --theme='light'"
if ngrok_auth:
  full_precision_str+=f"  --ngrok={ngrok_auth} --ngrok-region='auto'"
  half_precision_str+=f"  --ngrok={ngrok_auth} --ngrok-region='auto'"
if is_full_precision:
  !python launch.py {full_precision_str} #（解决精度不足但速度不够）
else:
  !python launch.py {half_precision_str} #半精度（速度提升1倍以上，但可能出现精度不足问题）
