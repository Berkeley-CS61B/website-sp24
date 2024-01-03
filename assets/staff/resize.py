import os
import tqdm
from PIL import Image

desired_height = 400

for name in tqdm.tqdm(os.listdir(".")):
    print(f"Resizing {name}")
    if not name.endswith('.jpg'):
        print("Filename doesn't end with .jpg")
        continue
    in_image = Image.open(name)
    os.remove(name)
    r = max(in_image.size)
    w, h = in_image.size

    desired_size = (int(float(w) * float(desired_height / h)), desired_height)

    out_image = in_image.resize(desired_size, resample=Image.Resampling.LANCZOS)
    out_image = out_image.convert("RGB")
    out_image.save(name.split(".")[0] + ".jpg", "JPEG")
