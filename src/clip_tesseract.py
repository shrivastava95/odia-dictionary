import clip
import torch
from pytesseract import pytesseract, Output
from PIL import Image
import os

lang = 'eng+ori'
custom_config = '--psm 3'
# classification_strings = ['image of odiya language text', 'image of english language text']
languages_clip = ['english', 'odiya']
languages_ocr = ['eng', 'ori']
image_path = 'GUI_sample_orig.png'

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model, preprocess = clip.load('ViT-B/16', device)

def string_template(language):
    return f'image of {language} language text'

def clip_classify_images(model, images, strings):
    logits_per_image, logits_per_text = model(
        torch.stack([preprocess(image) for image in images], dim=0).to(device),
        clip.tokenize(strings).to(device)
    ) # [N-img, N-txt], [N-txt, N-img]
    return logits_per_image.cpu().detach().numpy()

def coop_classify_images(model, images, strings):
    n_ctx = model.trainable_param.shape[0]

    # get image features
    image_features = model.encode_image(torch.stack([preprocess(image) for image in images], dim=0).to(device))
    image_features = image_features / image_features.norm(dim=-1, keepdim=True)
    
    # get text features
    class_texts_template = ['X ' * n_ctx + class_name for class_name in strings]
    class_features = model.encode_text_coop(clip.tokenize(class_texts_template).to(device)) # using the modded text encoder
    similarity = (100 * image_features @ class_features.T).softmax(dim=-1)
    return similarity.cpu().detach().numpy()

def cocoop_classify_images(model, images, strings):
    assert False, "Not Implemented" 

def reprocess(mode, idx, ocr_data, image, languages_clip, lamguages_ocr, offset=4):
    mapping = {
        'clip': clip_classify_images,
        'coop': coop_classify_images,
        'cocoop': cocoop_classify_images,
    }

    x, y, w, h = ocr_data['left'][idx], ocr_data['top'][idx], ocr_data['width'][idx], ocr_data['height'][idx]
    x0, y0, x1, y1 = (x - offset, y - offset, x + w + offset, y + h + offset)
    region = image.crop((x0, y0, x1, y1))

    classification_strings = [string_template(langname) for langname in languages_clip]
    logits_per_region = mapping[mode](   # clip_classify_images(
        model,
        [region],
        classification_strings
    )
    class_idx = logits_per_region.argmax(dim=1)[0]
    predicted_lang_ocr = languages_ocr[class_idx]
    word = pytesseract.image_to_string(region, 
                                       lang=predicted_lang_ocr, 
                                       config='--psm 8') # word level parsing
    return word


# dict_keys(['level', 'page_num', 'block_num', 'par_num', 'line_num', 'word_num', 'left', 'top', 'width', 'height', 'conf', 'text'])
def image_to_string_v2(img_path, lang, custom_config, mode='clip'):
    image = Image.open(img_path)
    data = pytesseract.image_to_data(image, lang=lang, config=custom_config, output_type=Output.DICT)
    total_text = []
    for i in range(len(data['level'])):
        if data['level'][i] == 5:
            data['text'][i] = reprocess(i, data, image, languages_clip, languages_ocr)
            total_text.append(data['text'][i] + ' ')
        elif data['level'][i] == 4:
            total_text.append('\n')
        elif data['level'][i] == 3:
            total_text.append('\n')
    total_text = ''.join(total_text)
    return total_text


print(image_to_string_v2(image_path, lang=lang, custim_config=custom_config, mode='clip')) # loading for coop  and cocoop not implemented yet so leave
# print('-------------------------------')
# print('-------------------------------')
# print('-------------------------------')
# print('-------------------------------')
# print(pytesseract.image_to_string(image_path, lang=lang, config=custom_config))
