import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"" #your tesseract bin archive
print(pytesseract.image_to_string(Image.open('img.png')))
