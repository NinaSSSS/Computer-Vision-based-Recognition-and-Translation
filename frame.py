import pytesseract 
from googletrans import Translator
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread("TRAIL2.png", cv2.IMREAD_GRAYSCALE)
(thresh, img_bw) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

cv2.imshow("BW", img_bw)
cv2.waitKey(0)

result = pytesseract.image_to_string(img_bw, lang='eng')
d = pytesseract.image_to_data(img_bw, output_type = pytesseract.Output.DICT, lang='eng')

n_boxes = len(d['level'])
text_pos_list = {}

for i in range(n_boxes):
    text = d['text'][i].strip()
    if len(text) == 0:
        continue    
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    text_pos_list[text] = (x, y, w, h)
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), -1)

trtext_pos_list = {}
p = Translator()

for text in text_pos_list.keys():
    p_translated = p.translate(text, dest='french')
    trtext_pos_list[str(p_translated.text)] = text_pos_list[text]

print(text_pos_list)
print(trtext_pos_list)

window_name = 'Image'
font = cv2.QT_FONT_NORMAL

for text in trtext_pos_list.keys():
    img = cv2.putText(img, text, (trtext_pos_list[text][0], trtext_pos_list[text][1]), font, 
                    trtext_pos_list[text][3]/30, (0, 0, 0), 1, cv2.LINE_AA)

cv2.imshow(window_name, img)
cv2.waitKey(0)