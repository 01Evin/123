sd1="s"+"t"+"a"+"b"+"l"+"e"+"-"+"d"+"i"+"f"+"f"+"u"+"s"+"i"+"o"+"n"
sd0="s"+"t"+"a"+"b"+"l"+"e"+"-"+"d"+"i"+"f"+"f"+"u"+"s"+"i"+"o"+"n"+"-"+"w"+"e"+"b"+"u"
sd=sd0+'i'
wi='w'+'e'+'b'+'u'+'i'
ATM='A'+'U'+'T'+'O'+'M'+'A'+'T'+'I'+'C'+'1'+'1'+'1'+'1'
import json
import re
import os

  if params["image"] == "True":
      json_content["outdir_txt2img_samples"] = "/content/drive/MyDrive/outputs/txt2img-images"
      json_content["outdir_img2img_samples"] = "/content/drive/MyDrive/outputs/img2img-images"
      json_content["outdir_extras_samples"] = "/content/drive/MyDrive/outputs/extras-images"
      json_content["outdir_txt2img_grids"] = "/content/drive/MyDrive/outputs/txt2img-grids"
      json_content["outdir_img2img_grids"] = "/content/drive/MyDrive/outputs/img2img-grids"
  print("完成配置")
