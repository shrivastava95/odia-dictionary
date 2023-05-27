# odia-dictionary
A repository for organizing contributions to the creation of an Odia Dictionary dataset for the Dictionary Augmented Translations project in C4GT'23.

## Description
This repository is for the purposes of building a parser that is able to read the Odia.Dictionary.pdf file and parse the definitions into a Dataset. The issues tab contains aspects of the current solution that need to be worked upon and refined, or added in the future.

## Dependencies / setup
**To be added**

## How to run
To parse the Odia Dictionary pdf:
1. create a .env file and add your openapi secret key to it. refer to `sample.env`.
2. `sh run1.sh` - reads the pdf and converts to 300 DPI high-resolution png images.
3. Open the png files generated in `./pages` with the Paint application and blank-out the unwanted letter section separator by selecting the relevant portion and pressing the delete key.
4. `sh run2.sh` - runs the remaining script files. **Description pending.**

