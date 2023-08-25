## Structure
**Folder**
- [GPT_output_merged](testgpt_compare_pdfs) - stores the output of [sender_merge.py](sender_merge.py) which is a merged text file of two OCR outputs(with 2 different psm settings) into a three-column table 
- [parsed_dicts_merged](testgpt_compare_pdfs) - stores the uncleaned merged data of 2 OCR outputs.

**Files**

- [maker.py](maker.py) -The code reads multiple CSV files from a source directory, merges them into a single dataframe, cleans the data by removing irrelevant columns and rows containing garbage values, and saves the cleaned dataframe as a CSV file in an output directory.
- [preprocess.py](pdfmaker.py) -The code processes text files in a directory (source_dir) by removing unnecessary text before the table starts. It reads each file, finds the index of the first occurrence of '|', truncates the file content from that index onwards, and saves the modified file.
- [sender_merge.py](sender_merge.py) -The code uses the OpenAI GPT-3.5-turbo model to merge and format two OCR outputs into a three-column table. It reads text files from two different source folders (source_folder and source_folder_2). For each text file, it sends a series of messages to the GPT-3.5-turbo model to instruct it on how to format the table and merge the outputs. The generated table is then saved to an output destination folder (output_destination). The code utilizes the tqdm library for progress tracking and includes error handling to handle exceptions during the process.
- [parsed_dicts_merged/filter_nouns.py](parsed_dicts_merged/filter_nouns.py) - creates noun-only csv from the dictionary.


