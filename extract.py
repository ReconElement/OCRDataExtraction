#write a simple script to extract info from sample_text.pdf but use pdf2image this time
from pdf2image import convert_from_path
import pytesseract
import os
from PIL import Image, ImageOps, ImageFilter
import re

cwd = os.getcwd() #gets the current directory
imagepath = str(cwd + r"\dataset_documents")
os.chdir(imagepath)
#converts the pdf to image
image = convert_from_path('data1.pdf',300, poppler_path=r"C:\Program Files\poppler-24.08.0\Library\bin")
image[0].save("sample_data.tiff")

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

#Applying edge detection filter
# image = image.filter(ImageFilter.FIND_EDGES)
image.show()
text = pytesseract.image_to_string(image)
print(text)
print(re.match(r"Date\s+", text))
print(text[5:])