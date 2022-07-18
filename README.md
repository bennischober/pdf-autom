# pdf-autom
A python tool to automate different tasks with pdfs.

## Current state
Pdf text can be saved to txt files (workflow: pdf => image => txt)

## Purpose
My plan is: analyze a large pdf file (might be scanned documents), cut each page and sort them.\
To achieve this, I have to use ``pdf2image`` to convert all pdfs to images. All files might be scanned documents, so the pdf will only contain a huge picture with text.\
To analyze the images, I use ``Tesseract OCR``. The data is saved to text file(s).\
In the next step I have to read all the text data and look for the specific sorting items. I might need some dictionaries to sort the specific pages (they might have to be sorted multiple times).\
In the last step I need to manipulate the original pdf (a copy) and reorder the pages / save the pages seperately (maybe a folder structure?)
