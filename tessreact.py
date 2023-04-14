import matplotlib.pyplot as plt
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('2.png')
plt.imshow(img)
img2char = pytesseract.image_to_string(img)
print(img2char)
