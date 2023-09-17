import json
import re
import os
import subprocess
import sys
wget_path = '/usr/bin/wget'

params = {}
    if params["image"] == "True":
        json_content["outdir_txt2img_samples"] = "/content/drive/MyDrive/outputs/txt2img-images"
        json_content["outdir_img2img_samples"] = "/content/drive/MyDrive/outputs/img2img-images"
        json_content["outdir_extras_samples"] = "/content/drive/MyDrive/outputs/extras-images"
        json_content["outdir_txt2img_grids"] = "/content/drive/MyDrive/outputs/txt2img-grids"
        json_content["outdir_img2img_grids"] = "/content/drive/MyDrive/outputs/img2img-grids"
    with open(f'{params["dir"]}/config.json', 'w') as configFile:
        json.dump(json_content, configFile, ensure_ascii=False, indent=4)
