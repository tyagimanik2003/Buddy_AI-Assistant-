import cv2
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import openai
import pyttsx3
import numpy as np
import pandas as pd
import requests
import imutils
from requests.auth import HTTPBasicAuth
import requests
import json
import sys


# OpenAI Key
openai.api_key = "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"
AIurl = "https://api.aivinya.education/api/public/aivachat"

# For Text to Speech
speech = pyttsx3.init()

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()


touristclassifier = Classifier("Dataset/Tourist/keras_model.h5", "Dataset/Tourist/labels.txt")
animalclassifier = Classifier("Dataset/Animals/keras_model.h5", "Dataset/Animals/labels.txt")
vegetableclassifier = Classifier("Dataset/Vegetable/Vegetable Final/keras_model.h5", "Dataset/Vegetable/Vegetable Final/labels.txt")
flowerclassifier = Classifier("Dataset/Flowers/keras_model.h5", "Dataset/Flowers/labels.txt")

offset = 20
imgSize = 300

url = "http://192.168.73.96:8080/shot.jpg"
username = "ABC"
password = "abc"


touristlabels = ['Alai Darwaza', 'Alai Minar', 'India Gate', 'Iron Pillar', 'Jamali Kamali Tomb', 'Lotus Temple', 'Qutub Minar', 'Red Fort']
animallabels = ['CHEETAH', 'CROCODILE', 'ELEPHANT', 'GIRAFFE', 'LION', 'PANDA', 'RHINO', 'TIGER', 'WOLF', 'ZEBRA']
vegetablelabels = ['Bean', 'Bitter Gourd', 'Bottle Gourd', 'Brinjal', 'Broccoli', 'Cabbage', 'Capsicum', 'Carrot', 'Cauliflower', 'Cucumber', 'Papaya', 'Potato', 'Pumpkin', 'Radish', 'Tomato']
flowerlabels = ['Bellflower', 'Black Eyed Susan', 'Daisy', 'Dandelion', 'Iris', 'Rose', 'Sunflower', 'Tulip', 'Water Lily', 'Carnation']

TouristimgBG = cv2.imread('Resources/mainpage.png')
AnimalimgBG = cv2.imread('Resources/mainpage.png')
VegetableimgBG = cv2.imread('Resources/mainpage.png')
FlowerimgBG = cv2.imread('Resources/mainpage.png')

while True:

    x=int(input("Enter Service:\n1.Tourist\n2.AnimalZoo\n3.VegetableMarket\n4.FlowerGarden\n5.Exit\nEnter your Choice: "))


    while True:
        # success, img = cap.read()
        img_resp = requests.get(url, auth = HTTPBasicAuth(username, password))
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1)
        imgOutput = img.copy()

        if x==1:
            imgBG = TouristimgBG
            prediction, index = touristclassifier.getPrediction(imgOutput, draw=False)
            labels = touristlabels
        elif x==2:
            imgBG = AnimalimgBG
            prediction, index = animalclassifier.getPrediction(imgOutput, draw=False)
            labels = animallabels
        elif x==3:
            imgBG = VegetableimgBG
            prediction, index = vegetableclassifier.getPrediction(imgOutput, draw=False)
            labels = vegetablelabels
        elif x==4:
            imgBG = FlowerimgBG
            prediction, index = flowerclassifier.getPrediction(imgOutput, draw=False)
            labels = flowerlabels

        if prediction[index]>0.9:
            print(prediction,index)
            cv2.putText(imgOutput, labels[index],(50,100),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255),4)
        imgBG[ 120: 120 + 480, 561:561 + 640 ] = imgOutput
        cv2.imshow("Image", imgBG)

        if cv2.waitKey(1) == ord('m'):
                # # For ChatGPT API
                print("OpenAI response is: ")
                aitext=f"Tell me about {labels[index]} in 30 words"
                payload = json.dumps({
                "text": aitext
                })
                headers = {
                'Content-Type': 'application/json'
                    }

                response = requests.request("POST", AIurl, headers=headers, data=payload)
                result=json.loads(response.text)
                answer=result["res"]
                print(answer)
                speech.say(answer)
                speech.runAndWait()
        if cv2.waitKey(1) == ord('q'):
            break
        
    cv2.destroyAllWindows()
    if x == 5:
        sys.exit


