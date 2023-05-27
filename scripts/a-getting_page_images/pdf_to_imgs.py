from pdf2image import convert_from_path
from tqdm import tqdm
pages = convert_from_path('Odia.Dictionary.pdf', 300, poppler_path=r'C:\ai_sem_7\poppler-0.68.0_x86\poppler-0.68.0\bin')
for i, page in enumerate(tqdm(pages)):
    page.save(f'pages/page{i}.png', 'PNG')