from PIL import Image
import os
from tqdm import tqdm

input_folder = 'contour_boxing/pages'
output_folder = 'contour_boxing/pages_processed'
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

for i, img_path in enumerate(tqdm(os.listdir('pages'))):
    if int(img_path.split('.')[0][4:]) in range(6, 88):
        if img_path.endswith('.png'):
            img = Image.open(os.path.join(input_folder, img_path))
            imgs = [
                img.crop(( 130,  250,  830,  3050)),
                img.crop(( 855,  250, 1569,  3050)),
                img.crop((1592,  250, 2336,  3050)),
            ]
            for i, im in enumerate(imgs):
                path = os.path.join(output_folder, img_path.split(".")[0] + f"_{i}." + img_path.split(".")[-1])
                im.save(path)
        
        
