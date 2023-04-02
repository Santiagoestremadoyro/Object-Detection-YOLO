import streamlit as st
import cv2
import tempfile

# Leer el archivo de video
video_file = st.file_uploader("Cargar video", type=["mp4", "avi", "mov"])
if video_file is not None:
    # Guardar el archivo en un directorio temporal
    temp_video = tempfile.NamedTemporaryFile(delete=False)
    temp_video.write(video_file.read())
    temp_video_path = temp_video.name

    # Crear el objeto VideoCapture de OpenCV
    cap = cv2.VideoCapture(temp_video_path)

    # Leer el modelo de detección y la lista de clases
    net = cv2.dnn.readNet("model_dnn/yolov4-tiny.weights", "model_dnn/yolov4-tiny.cfg")
    classes = []
    with open("model_dnn/classes.txt", "r") as file_object:
        for class_name in file_object.readlines():
            class_name = class_name.strip()
            classes.append(class_name)
    model = cv2.dnn_DetectionModel(net)
    model.setInputParams(size=(320, 320), scale=1/255)

    # Obtener la información del video
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    # Crear el objeto VideoWriter de OpenCV para guardar el video resultante
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter("output.mp4", fourcc, fps, frame_size)

    # Iterar sobre cada frame del video
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detectar objetos en el frame
        class_ids, scores, boxes = model.detect(frame, confThreshold=0.3, nmsThreshold=0.4)

        # Dibujar los bboxs y los nombres de las clases
        for class_id, score, bbox in zip(class_ids, scores, boxes):
            x, y, w, h = bbox
            class_name = classes[class_id[0]-1]
            color = (0, 255, 0)
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, thickness=2)
            cv2.putText(frame, class_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness=2)

        # Convertir la imagen a bytes
        _, img_encoded = cv2.imencode(".png", frame)

        # Mostrar la imagen en el dashboard
        st.image(img_encoded.tobytes(), channels="BGR")

        # Guardar el frame en el video resultante
        out

