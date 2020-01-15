from PIL import Image  # Importando o módulo Pillow para abrir a imagem no script

from pytesseract import image_to_string  # Módulo para a utilização da tecnologia OCR

print(image_to_string(Image.open('teste.jpg')))
