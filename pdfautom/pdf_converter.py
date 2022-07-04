from pathlib import Path
from PIL import Image
import pytesseract
from pdf2image import convert_from_path


def read_text(pdf_path, poppler_path, image_path):
    print("LOL")
    # first check, if pdf contains text or images
    # pages = None
    # with pdfplumber.open(pdf_path) as pdf:
    #     pages = pdf.pages
    #     fp = pdf.pages[0]
    #     t = fp.extract_text()
    #     if len(t) > 0:
    #         print(t)
    #     else:
    #         print('No text found!')

    #     print(len(pages))

    #     for page in pages:
    #         print(page.extract_text())


def create_images(pdf_path, poppler, image_path):
    # for path not exist errors:
    # https://stackoverflow.com/questions/8933237/how-to-find-if-directory-exists-in-python
    # https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory

    pages = convert_from_path(pdf_path, poppler_path=poppler)

    image_counter = 1

    for page in pages:
        path = Path.joinpath(image_path, "page_"+str(image_counter)+".jpg")
        page.save(str(path), 'JPEG')
        image_counter = image_counter + 1

    return image_counter


def read_images(num_images, tesseract_path, image_path, text_path):
    # set path for tesseract
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    filelimit = num_images - 1
    outfile = Path.joinpath(text_path, "out_text.txt")
    f = open(outfile, "a", encoding="UTF8")

    for i in range(1, filelimit + 1):
        path = Path.joinpath(image_path, "page_"+str(i)+".jpg") # wrong image number! num_images-1
        text = str(((pytesseract.image_to_string(Image.open(str(path))))))
        text = text.replace('-\n', '')
        f.write(text)

    f.close()


def convert_pdfs(pdf_path, poppler_path, tesseract_path, image_path, text_path):
    num_images = create_images(pdf_path, poppler_path, image_path)
    read_images(num_images, tesseract_path, image_path, text_path)
