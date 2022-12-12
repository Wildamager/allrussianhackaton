import cv2
from matplotlib import pyplot as plt
import numpy as np
import pytesseract
import time
import os
from operator import itemgetter
import re
import pkg_resources

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe "
carplate_haar_cascade = cv2.CascadeClassifier ('apps\camerastream\haarcascade_russian_plate_number.xml')

#####Setting function for identifying the vehicle number#####
def carplate_detect(image,carplate_haar_cascade):
    carplate_overlay = image.copy() 
    carplate_rects = carplate_haar_cascade.detectMultiScale(carplate_overlay,scaleFactor=1.1, minNeighbors=5)
    for x,y,w,h in carplate_rects: 
        cv2.rectangle(carplate_overlay, (x,y), (x+w,y+h), (255,0,0), 5) 
    return carplate_overlay

#Function to get only the license plate area itself
def carplate_extract (image,carplate_haar_cascade): 
    carplate_rects = carplate_haar_cascade.detectMultiScale (image, scaleFactor = 1.1, minNeighbors = 5)
    carplate_img = []
    for x, y, w, h in carplate_rects: 
        carplate_img = image [y + 15: y + h-10, x + 15: x + w-20] 
    return carplate_img

#Zoom function for further processing 
def enlarge_img(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    return resized_image

def detection(img, carplate_haar_cascade):
    img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    try:
        carplate_extract_img = carplate_extract(img_rgb,carplate_haar_cascade)
        if not np.array_equal([],carplate_extract_img):
            carplate_extract_img = enlarge_img(carplate_extract_img, 150)   
            return carplate_extract_img
        else:
            return []
    except:
        return []

def predict(img):

    img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    config="-c tessedit_char_whitelist=ABCEHKMOPTXY0123456789 --psm 7"
    data = (pytesseract.image_to_string(img, config=config))
    data = data.upper().replace(" ", "").strip()

    if len(data)>=6:
        data = (data[0:6])
        
        buk = itemgetter(0, 4, 5)(data)
        chis = itemgetter(1, 2, 3)(data)
        chis = (''.join(chis))
        buk = (''.join(buk))
        buk = buk.replace('0','O')
        chis = chis.replace('O','0')
        data = buk[0]+chis+buk[1:3]
        
        result = re.findall(r"[A-Z]\d\d\d[A-Z][A-Z]", data)
        if len(result) != 1:
            return None
        if result[0] == data:
            print(data)
            return data
        else:
            return None

def main(camera):

    url = 'rtsp://192.168.1.54:554//user=admin_password=662_channel=1_stream=0.sdp?real_stream'
    vid = cv2.VideoCapture(url)
    while(vid.isOpened()):
        ret, frame = vid.read()
        if ret:

            img_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            # detected_carplate_img = carplate_detect(img_rgb, carplate_haar_cascade)

            carplate_extract_img = carplate_extract(img_rgb, carplate_haar_cascade)
            if not np.array_equal([],carplate_extract_img):
                carplate_extract_img = enlarge_img(carplate_extract_img, 150)
                return predict(carplate_extract_img)
   
            else:
                return "number didnt found" 
    