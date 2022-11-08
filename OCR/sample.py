import pytesseract



img_path = 'test.png'
lang = 'eng'
pytesseract.pytesseract.tesseract_cmd = "D:\MVS_Code\zocket\tesseract.exe"
print(img_path)
text = pytesseract.image_to_string(img_path, lang=lang)

print(text)