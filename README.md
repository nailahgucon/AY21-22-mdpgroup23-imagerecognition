# CZ3004 Multidisplinary Project - Image Recognition

Experimented with 2 models, YOLOv4-tiny and YOLOv5, ended up going with the YOLOv5 model as it performed better under extreme lighting situations outdoors.
Image recognition was done on my PC (not in the RPi) & a REST API with Flask was used to load the model at the start of the run and to pass the image ID of the image detected to the RPi. 

**My Dataset**
- Images and text files with annotations: https://www.kaggle.com/nailahgpgucon/
- Annotation Tool used: https://github.com/tzutalin/labelImg (Download binary file found in Releases Section)
<br>

**Training the Model** 

Depending on your choice of YOLOv4 and YOLOv5, Roboflow provides a Google Colab notebook that helps to train your model.
- https://blog.roboflow.com/training-yolov4-on-a-custom-dataset/
- https://blog.roboflow.com/how-to-train-yolov5-on-a-custom-dataset/

*Reason for choice: It's much easier to use as you do not have to install any dependencies and do not require an NVIDIA GPU. However, there's a GPU limit, and hence based on my experience, training can only be done 3-4hrs a day.*

<br>

**Deployment to PC and Connection to RPI**

##### Prerequisites:
- Python 3.7** (https://www.python.org/downloads/) 
- Anaconda Prompt (https://docs.anaconda.com/anaconda/install/windows/)
- Git Bash (https://git-scm.com/)

** May work with other Python versions but had the least issues with installation of other required libraries with Python 3.7

##### Procedure:
TO-DO
