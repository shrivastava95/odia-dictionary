# odia-dictionary
A repository for organizing contributions to the creation of an Odia Dictionary dataset for the Dictionary Augmented Translations project in C4GT'23.

## Description
This repository is for the purposes of building a parser that is able to read the Odia.Dictionary.pdf file and parse the definitions into a Dataset. The issues tab contains aspects of the current solution that need to be worked upon and refined, or added in the future.

## Dependencies / setup
1. [pdf2image setup](src/a-getting_page_images/SETUP.md)
2. [Tesseract API setup](src/c-images_to_pdfs_with_text/SETUP.md)
3. [PyPDF2 PDF Reader setup](src/d-read_pdfs_with_text/SETUP.md)
4. [OpenAI API setup](src/e-gpt_api_sender/SETUP.md)

## How to run
To parse the Odia Dictionary pdf:
<details>

<summary>

#### 1. `python src/a-getting_page_images/pdf_to_imgs.py`

</summary>

 - Converts each page of the [Odia Dictionary PDF](Odia.Dictionary.pdf) to a 300 DPI image stored in [pages](pages).

</details>
<details>

<summary>

#### 2. Open the png files generated in `./pages` with the Paint application and blank-out the unwanted letter section separator by selecting the relevant portion and pressing the delete key.
#### 3. `python src/b-cropping_page_images/cropper.py`

</summary>

 - Crops out the columns of interest from pages 6-87. Outputs stored in [pages_processed](pages_processed)

</details>
<details>

<summary>

#### 4. `python src/c-images_to_pdfs_with_text/pdfmaker.py`

</summary>

 - Runs Tesseract OCR on the images in [pages_processed](pages_processed). Outputs PDFs to [parsed_pdfs](parsed_pdfs)

</details>
<details>

<summary>

#### 5. `python src/d-read_pdfs_with_text/reader.py`

</summary>

 - Gets unstructured OCR text output from PDFs in [parsed_pdfs](parsed_pdfs). Outputs .txt files to [parsed_texts](parsed_texts)

</details>
<details>

<summary>

#### 6. `rm GPT_outputs/*`

</summary>

 - the GPT outputs folder must be emptied as the API will not be called to replace text files already present in the folder. (refer to [sender.py](src/e-gpt_api_sender/sender.py))

</details>
<details>

<summary>

#### 7. `python src/e-gpt_api_sender/sender.py`

</summary>

 - Calls the GPT API to structure the raw OCR text output files in [parsed_texts](parsed_texts). Outputs .txt files to [GPT_outputs](GPT_outputs)

</details>
<details>

<summary>

#### 8. `python src/f-dataframe_maker/preprocess.py`

</summary>

 - Removes the 1st line of every .txt file in [GPT_outputs](GPT_outputs) if it does not begin with the appropriate delimiter `"|"`. **Run this command 2-3 times** until every .txt file in the gpt outputs folder starts with a CSV file header.
#### 9. `python src/f-dataframe_maker/maker.py`

</summary>

 - Compiles [GPT_outputs](GPT_outputs) to the desired .csv - [parsed_dicts/parsed_dict_very_unclean.csv](parsed_dicts/parsed_dict_very_unclean.csv)

</details>






## Structure
**Folders**
- `GPT_outputs` - stores parsed & formatted text tables
- `pages` - stores images for every page of the pdf
- `pages_processed` - stores cleaned and cropped column images for pages 6-88
- `parsed_dicts` - stores the final output csv
- `parsed_pdfs` - stores the intermediate pdfs generated using Tesseract OCR for each processed image
- `parsed_texts` - stores the intermediate texts generated from the intermediate pdfs
- `src` - stores the scripts necessary for parsing the dictionary.

**Files**
- `.env` - stores the OPENAPI_SECRET_KEY variable
- `Odia.Dictionary.pdf` - the pdf to be parsed
- `run1.sh` - converts the pdf to images
- `run2.sh` - executes the rest of the scripts for parsing to a basic dictionary
- `sample.env` - a reference for how the .env file should look (without the key)
