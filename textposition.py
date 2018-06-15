import cv2
import pytesseract
import re
img = cv2.imread('sample/3.png')
#cv2.imshow('original',img)

#text = pytesseract.image_to_string(img, lang = "eng")
text1 = pytesseract.image_to_boxes(img)
print (text1)
# print('Length is: ' + str(len(text)))
# # labels = text.split()
# # counter = 1
# # for label in labels:
# #     if (label + counter).isupper():
# #         print('Label' + str(counter) + ':' + label + (label+counter))
# #     counter += 1
#
#
# def split_uppercase(value):
#     return re.sub(r'([A-Z])', r' \1', value)
#
# print(split_uppercase(text))

