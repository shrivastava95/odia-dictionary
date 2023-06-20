import pytesseract
from tqdm import tqdm
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import enchant
import html

spellcheck = enchant.Dict('en_US')

# remove this line on linux.
pytesseract.pytesseract.tesseract_cmd = f"C:/Program Files/Tesseract-OCR/tesseract.exe"

# different psm mode can change the behaviour of parsing.
# refer to documentation for further details.
psm_mode = 6
psm_mode_2 = 6
config = f'--psm {psm_mode}'
config2 = f'--psm {psm_mode_2}'
source_pdf_folder = 'contour_boxing/pages_processed'
target_folder = 'contour_boxing/parsed_texts'
lang='ori+eng'
lang1='eng'
lang2='ori'
tolerance = 5 # controls how "strict" the definition of being "contained" is in the context of bounding boxes. 
if not os.path.exists(target_folder): 
    os.mkdir(target_folder)

def check_lang1(character): # character-level language check. Currently implemented for English.
    if ord(character) in range(65, 90+1) or ord(character) in range(97, 122+1):
        return True
    return False

def check_lang2(character): # character-level language check. Currently implemented for Odiya.
    if ord(character) in range(2816, 2943+1):
        return True
    return False

def read_image(img_path):
    image = cv2.imread(img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    return image

def compare_proposals(text1, text2):
    score_lang1 = sum([check_lang1(ci) for ci in text1]) - len(text1)
    score_lang2 = sum([check_lang2(ci) for ci in text2]) - len(text2)
    # if text1 == 'GIG':
    #     print(text1, text2, score_lang1, score_lang2)
    if len(text1) <= 3:
        if score_lang2 >= 0:
            best_box_text = text2
        elif spellcheck.check(text1):
            best_box_text = text1
        else:
            best_box_text = text2
    else:
        score_lang1 += len(text1) * (2/3)
        score_lang2 += len(text2) * (2/3)
        if score_lang1 >= 0 and score_lang2 >= 0:
            if spellcheck.check(text1):
                best_box_text = text1
            else:
                best_box_text = text2
        elif score_lang2 >= 0:
            best_box_text = text2
        elif score_lang1 >= 0:
            best_box_text = text1
        else:
            best_box_text = text2
    return best_box_text


for i, image_path in enumerate(tqdm(os.listdir(source_pdf_folder))):
    # if 'page8_1' not in image_path:
    #     continue
    if int(image_path.split('.')[0].split('_')[0][4:]) in range(6, 88):      # only parsing pages 6 - 87, inclusive
        source_image_path = os.path.join(source_pdf_folder, image_path)       # for example: source_pdf_folder/page6_0.png
        target_image_path = os.path.join(target_folder, f'{image_path}.txt')  # for example: target_folder/page6_0.png.txt

        page_image = read_image(source_image_path)
        h, w = page_image.shape # assumes grey image
        boxes = pytesseract.image_to_data(page_image, config=config, lang=lang, output_type=pytesseract.Output.DICT)
        n_boxes = len(boxes['level'])
        # print(boxes)
        box_proposals = []
        for box_idx in range(n_boxes):
            (x, y, w, h) = (
                boxes['left'][box_idx]  ,
                boxes['top'][box_idx]   ,
                boxes['width'][box_idx] ,
                boxes['height'][box_idx],
            )
            box_proposals.append([x, y, w, h])
        
        box_proposals = np.unique([
                ' '.join([str(coordinate) for coordinate in [x, y, w, h]]) 
                for x, y, w, h in box_proposals
        ])
        box_proposals = [list(map(int, string.split())) for string in box_proposals]
        # print(box_proposals)
        contains = [[0 for i in range(len(box_proposals))] for i in range(len(box_proposals))]
        for idx1, (x1, y1, w1, h1) in enumerate(box_proposals):
            for idx2, (x2, y2, w2, h2) in enumerate(box_proposals):
                if  x1       <=   x2 \
                and y1       <=   y2 \
                and x1 + w1  >=   x2 + w2 \
                and y1 + h1  >=   y2 + h2:
                    contains[idx1][idx2] = 1
                    # pass
        
        reduced_box_proposals = [
                                    [x, y, w, h] 
                                    for idx, (x, y, w, h) 
                                    in enumerate(box_proposals)
                                    if np.sum(contains[idx]) <= 1 # if a bounding box contains other bounding boxes than itself then we dont consider it
                                ]
        # print(reduced_box_proposals)
        # for x, y, w, h in reduced_box_proposals:
        #     cv2.rectangle(page_image, (x - tolerance, y - tolerance), (x + w + tolerance, y + h + tolerance), (0, 255, 0), 2)
        # plt.imshow(page_image)
        # plt.show()
        # page_image = read_image(source_image_path)

        #### algo to merge overlapping vertical spans
        tracker = set([])
        spans = []
        # y+h before y so that segments can fully close in case of coinciding overlaps
        reduced_box_proposals = sorted(reduced_box_proposals, key=lambda x: x[1] + x[3])
        store = [[y+h, idx] for idx, (x, y, w, h) in enumerate(reduced_box_proposals)] + [[y, idx] for idx, (x, y, w, h) in enumerate(reduced_box_proposals)]
        store = sorted(store, key=lambda x: x[0])
        for y, idx in store:
            if len(tracker) == 0:
                spans.append([])
                spans[-1].append(idx)
                tracker.add(idx)
            else:
                if idx not in tracker:
                    spans[-1].append(idx)
                    tracker.add(idx)
                else:
                    tracker.remove(idx)
        
        spans = [sorted(span, key=lambda x: reduced_box_proposals[x][0]) for span in spans]
        # print(spans)

        with open(target_image_path, 'w') as f:
            f.write('')
        # with open(target_image_path, 'w') as f:
        #     f.write('Line Number | OCR English | OCR Odia')
        for line_num, span in enumerate(spans):
            with open(target_image_path, 'a') as f:
                f.write('\n')
            for x, y, w, h in [reduced_box_proposals[idx] for idx in span]:
                with open(target_image_path, 'a+b') as f2:
                    cropped_image = page_image[y-tolerance:y+h+tolerance, 
                                               x-tolerance:x+w+tolerance]
                    # plt.imshow(cropped_image)
                    # plt.show()
                    box_text_lang1 = html.unescape(pytesseract.image_to_string(cropped_image, 
                                                                               lang=lang1, 
                                                                               config=config2)).replace('\u200c', '').strip()
                    box_text_lang2 = html.unescape(pytesseract.image_to_string(cropped_image, 
                                                                               lang=lang2, 
                                                                               config=config2)).replace('\u200c', '').strip()
                    try:
                        best_box_text = compare_proposals(box_text_lang1, box_text_lang2)
                    except Exception as e:
                        print(e)
                        # plt.imshow(cropped_image)
                        # plt.show()
                        continue

                    box_text = " " + best_box_text + " "
                    # print(" " + box_text + " ")
                    f2.write(box_text.encode())
        # break
        