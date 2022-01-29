from pathlib import Path
from pdfautom.config_parser import get_libpaths, get_readpaths, get_outpaths
from pdfautom.pdf_converter import convert_pdfs


def main():
    libs = get_libpaths()
    read = get_readpaths()
    out = get_outpaths()

    # create paths
    root = Path(__file__).parent
    images = Path.joinpath(root, out['images'])
    text = Path.joinpath(root, out['text'])

    dir = Path.joinpath(root, read['Pdf'])

    # iterate over all pdfs
    for index, filename in enumerate(dir.glob('**/*.pdf')):
        # ToDo: paths for images and text should change => make subfolder and use pdf name
        pdf_path = Path.joinpath(dir, filename)
        convert_pdfs(str(pdf_path), libs['Poppler'], libs['Tesseract'], images, text)


if __name__ == "__main__":
    main()
