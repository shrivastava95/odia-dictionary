# odia-dictionary
A repository for organizing contributions to the creation of an Odia Dictionary dataset for the Dictionary Augmented Translations project in C4GT'23.

## Description
This repository is for the purposes of building a parser that is able to read the Odia.Dictionary.pdf file and parse the definitions into a Dataset. The issues tab contains aspects of the current solution that need to be worked upon and refined, or added in the future.

## Dependencies / setup
**To be added** until then, simply go through all the files in `scripts` and figure out the different packages to install and other native installations.

## How to run
Note: do not run the optional steps unless the `pages` directory is empty.

To parse the Odia Dictionary pdf:
1. (OPTIONAL) create a .env file and add your openapi secret key to it. refer to `sample.env`.
2. (OPTIONAL) `sh run1.sh` - reads the pdf and converts to 300 DPI high-resolution png images.
3. Open the png files generated in `./pages` with the Paint application and blank-out the unwanted letter section separator by selecting the relevant portion and pressing the delete key.
4. `sh run2.sh` - runs the remaining script files. **Description pending.**

## Structure
**Folders**
- `GPT_outputs` - stores parsed & formatted text tables
- `pages` - stores images for every page of the pdf
- `pages_processed` - stores cleaned and cropped column images for pages 6-88
- `parsed_dicts` - stores the final output csv
- `parsed_pdfs` - stores the intermediate pdfs generated using Tesseract OCR for each processed image
- `parsed_texts` - stores the intermediate texts generated from the intermediate pdfs
- `scripts` - stores the scripts necessary for parsing the dictionary.

**Files**
- `.env` - stores the OPENAPI_SECRET_KEY variable
- `Odia.Dictionary.pdf` - the pdf to be parsed
- `run1.sh` - converts the pdf to images
- `run2.sh` - executes the rest of the scripts for parsing to a basic dictionary
- `sample.env` - a reference for how the .env file should look (without the key)
