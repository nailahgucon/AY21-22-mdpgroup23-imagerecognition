#!/bin/sh
cd ~ 
cd C:\\Users\\naila\\OneDrive\\Desktop\\mdp23-yolov5\\yolov5-fastapi
conda activate mdp23-yolov5-app
curl -X POST "http://localhost:8000/object-to-json" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@image.jpg;type=image/jpg"
curl -X POST "http://localhost:8000/object-to-img" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@image.jpg;type=image/jpg" --output test.jpg