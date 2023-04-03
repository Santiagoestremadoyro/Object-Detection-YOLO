# Sidewalk Obstacle Detection and Navigation Assistance for the Visually Impaired

This project aims to develop a live object detection system to assist blind people on the street. The system uses the Yolo model to detect a variety of objects in real time, such as people, vehicles, traffic signs, street furniture, etc. In addition, the system can also detect and remember important places previously selected by the user.

<p align="center">
  <img src="https://github.com/Santiagoestremadoyro/Object-Detection-YOLO/blob/main/img/yolov%20model.jpg?raw=true" width="3000">
</p>

# Installation

To run this project, you will need to have Python 3.10.10 or later installed. You can install the required Python packages by running the following command:

```python
   pip install -r requirements.txt
```
 
# Usage

To run the Streamlit app, run the following command:

```python
   streamlit run streamlit.py
```
# Functionalities
- Live detection of objects on the street, including people, vehicles, traffic signs and street furniture.
- Reminder of important places previously selected by the user.
- Ability to recognize people known by the user.
- Ability to detect obstacles in the user's path and provide audible alerts in real time.
- Intuitive and easy to use user interface.

# Used technology
- Python programming language.
- Yolo model for object detection.
- COCO data set for training the model.
- Computer vision libraries, such as OpenCV and TensorFlow.

# Model (YOLO)

<p align="center">
  <img src="https://github.com/Santiagoestremadoyro/Object-Detection-YOLO/blob/main/img/yolov%20model.jpg?raw=true" width="3000">
</p>

The YOLO (You Only Look Once) model is an object detection model that uses a single neural network to simultaneously predict the classes and locations of objects in an image. Unlike other object detection approaches that require multiple processing steps, YOLO detects in a single pass.

The model works by dividing the input image into a grid and generating bounding boxes for each cell in the grid. Each bounding box predicts the probability that it contains an object and the coordinates of the rectangle surrounding the object. In addition, the model also predicts the probabilities of each object class for each bounding box.

In the live object detection project for assisting blind people, the YOLO model is used to detect objects in real time from the camera image. The model has been pre-trained using the COCO dataset and can detect up to 80 different object classes. Currently, the project can detect objects in real time, but the implementation of the functionality of detecting the distance of detected objects is being worked on.

# Project Updates

After the project is delivered, my goal is to continue working on it and make it even better. I think this is a very interesting and useful idea that could be implemented in real life to help blind people. In the future, I would like to explore the possibility of using more advanced artificial intelligence techniques to improve the accuracy and efficiency of the detection model.

- [ ] Calculation of the distance of the detected objects
- [ ] create an app for the convenience of the user