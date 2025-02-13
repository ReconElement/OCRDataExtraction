#write a simple script to extract info from sample_text.pdf but use pdf2image this time
from pdf2image import convert_from_path
import pytesseract
import os
from PIL import Image, ImageOps, ImageFilter
import re

#makesure to include the extensions i.e, .pdf, .jpeg etc in file name
def extract_text(filename: str) -> str:
    cwd = os.getcwd() #gets the current directory
    imagepath = str(cwd + r"\dataset_documents")
    os.chdir(imagepath)
    print(imagepath)
    #converts the pdf into image
    if(filename.endswith('.pdf')):
        image = convert_from_path(fr'{filename}',300, poppler_path=r"C:\Program Files\poppler-24.08.0\Library\bin")
        image[0].save("sample_data.tiff")
    elif(filename.endswith(".jpeg") or filename(".jpg")):
        #change the image type from jpeg to tiff
        image = Image.open(fr"{filename}")
        image.save("sample_data.tiff",'TIFF')
    else:
        raise TypeError("File is of not the prescribed type")
    
    #define path to tesseract.exe
    path_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    #point tesseract cmd to tesseract.exe executable
    try:
        pytesseract.tesseract_cmd = path_tesseract
    except:
        print("Tesseract not found or installed")
    
    #open image and convert it to grayscale
    image = Image.open("sample_data.tiff").convert('L')
    
    #resizing the image for better accuracy
    scale_factor = 2
    image = image.resize((image.width*scale_factor, image.height*scale_factor), resample=Image.LANCZOS)
    
    #applying tesseract ocr and returning the string
    text = pytesseract.image_to_string(image)
    return text

# text = extract_text("data1.pdf")
# print(text)
