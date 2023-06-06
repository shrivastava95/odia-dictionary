from PIL import Image
import os
from tqdm import tqdm

for i, img_path in enumerate(tqdm(os.listdir('pages'))):
    if int(img_path.split('.')[0][4:]) in range(10, 364):
        if img_path.split('.')[-1] == 'png':
            img = Image.open(f'pages/{img_path}')
            imgs = [
                img.crop(( 130,  250,  830,  3050)),
                img.crop(( 855,  250, 1569,  3050)),
                img.crop((1592,  250, 2336,  3050)),
            ]
            for i, im in enumerate(imgs):
                path = f'pages_processed/{img_path.split(".")[0] + f"_{i}." + img_path.split(".")[-1]}'
                # print(path)
                im.save(path)
        
        
