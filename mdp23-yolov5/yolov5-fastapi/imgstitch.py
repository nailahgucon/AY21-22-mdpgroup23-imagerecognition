from __future__ import print_function
import os
import cv2
# import numpy
import glob

from PIL import Image

# files = [
#   'C:\\Users\\naila\\OneDrive\\Desktop\\YOLOv4-Object-Detection-API-Server\\detections\\img1.jpg',
#   'C:\\Users\\naila\\OneDrive\\Desktop\\YOLOv4-Object-Detection-API-Server\\detections\\img2.jpg',
#   'C:\\Users\\naila\\OneDrive\\Desktop\\YOLOv4-Object-Detection-API-Server\\detections\\img3.jpg',
#   'C:\\Users\\naila\\OneDrive\\Desktop\\YOLOv4-Object-Detection-API-Server\\detections\\img4.jpg',
#   'C:\\Users\\naila\\OneDrive\\Desktop\\YOLOv4-Object-Detection-API-Server\\detections\\img5.jpg',
#   'C:\\Users\\naila\\OneDrive\\Desktop\\YOLOv4-Object-Detection-API-Server\\detections\\img6.jpg',
#   'C:\\Users\\naila\\OneDrive\\Desktop\\YOLOv4-Object-Detection-API-Server\\detections\\\img7.jpg',
#   'C:\\Users\\naila\\OneDrive\\Desktop\\YOLOv4-Object-Detection-API-Server\\detections\\img8.jpg']

dir = "C:\\Users\\naila\\OneDrive\\Desktop\\mdp23-yolov5\\yolov5-fastapi\\images\\to-be-stitched" # current directory
ext = ".jpg"

pathname = os.path.join(dir, "*" + ext)
files = [img for img in glob.glob(pathname)]
#print(files)

result = Image.new("RGB", (3200, 1400))

for index, file in enumerate(files):
  path = os.path.expanduser(file)
  img = Image.open(path)
  img.thumbnail((800, 600), Image.ANTIALIAS)
  x = index // 2 * 800
  y = index % 2 * 600
  w, h = img.size
  result.paste(img, (x, y, x + w, y + h))

result.save(os.path.expanduser('C:\\Users\\naila\\OneDrive\\Desktop\\mdp23-yolov5\\yolov5-fastapi\\images\\to-be-stitched\\stitched-image.jpg'))

final_img = Image.open('C:\\Users\\naila\\OneDrive\\Desktop\\mdp23-yolov5\\yolov5-fastapi\\images\\to-be-stitched\\stitched-image.jpg')
final_img.show()