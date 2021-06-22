import cv2
import pytesseract	
img = cv2.imread(r'C:\Users\dell\Pictures\Blob3.png')
pytesseract.pytesseract.tesseract_cmd = (r'C:\Program Files\Tesseract-OCR\tesseract.exe')
result = pytesseract.image_to_string(img)
print(result)
		