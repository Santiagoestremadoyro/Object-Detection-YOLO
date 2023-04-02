import streamlit as st
import cv2
import numpy as np
import tempfile

#Opencv DNN
net = cv2.dnn.readNet("../model/dnn_model/yolov4-tiny.weights", "../model/dnn_model/yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size =(320, 320), scale=1/255)

#cargar class list
classes = []
with open("../model/dnn_model/classes.txt", "r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)

st.sidebar.header("Cargar video")
video_file = st.sidebar.file_uploader("", type=["mp4", "avi", "mov"])

# Guardar el archivo en un directorio temporal
temp_video = tempfile.NamedTemporaryFile(delete=False)
temp_video.write(video_file.read())
temp_video_path = temp_video.name

st.title("Detector de objetos")
st.write("Carga un video para detectar objetos en tiempo real")

if st.button("Detectar objetos") and video_file is not None:
    #iniciar camara
    cap = cv2.VideoCapture(temp_video_path)
    #Parametros de la camara
    #cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    #cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


FRAME_WINDOW = st.image([])    

while True:
   ret, frame = cap.read()

   print("-----------------------------------------------------------------------------------")

   #object detection
   print(frame)
   (class_ids, score, bboxes) = model.detect(frame)


   if len(class_ids) == 0:
     print("No se detectaron objetos en este frame.")

   for class_id, score, bbox in zip(class_ids, score, bboxes):
     (x,y,w,h) = bbox
   class_name = classes[class_id]

   #Colocar el nombre de las clases
   cv2.putText(frame, class_name, (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (200, 0, 50), 2)
   #colocar el rectangulo
   cv2.rectangle(frame, (x,y), (x+w, y+h), (200, 0, 50), 3)

   if frame.shape[0] > 0 and frame.shape[1] > 0:
      FRAME_WINDOW.image(frame)