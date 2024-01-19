import os

import PIL
import tqdm
from PIL import Image

desired_height = 400

for name in tqdm.tqdm(os.listdir(".")):
    try:
        print(f"Resizing {name}")
        if not name.endswith('.jpg'):
            print("Filename doesn't end with .jpg")
            continue
        in_image = Image.open(name)
        os.remove(name)
        r = max(in_image.size)
        w, h = in_image.size

        desired_size = (int(float(w) * float(desired_height / h)), desired_height)
        if desired_size[0] < desired_size[1]:
            desired_size = (desired_height, int(float(h) * float(desired_height / w)))


        out_image = in_image.resize(desired_size, resample=Image.Resampling.LANCZOS)
        out_image = out_image.convert("RGB")
        out_image.save(name.split(".")[0] + ".jpg", "JPEG")
    except PIL.UnidentifiedImageError as e:
        print(e)


"""
Better script to resize: 

shopt -s nullglob
for i in *.{png,PNG,gif,GIF,heic,HEIC}; do convert "$i" "${i%.*}.jpg"; done
for i in *.{JPG,jpeg,JPEG,jfif,JFIF}; do mv "$i" "${i%.*}.jpg"; done
mogrify -resize '512x512^>' -gravity center -crop '512x512+0+0' -strip *.jpg
shopt -u nullglob
"""
