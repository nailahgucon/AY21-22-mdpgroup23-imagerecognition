import socket
import time
import os
import cv2
import subprocess
from readID import readID
from returnTest import *
from PIL import Image
import subprocess
import shutil
import ast

os.chdir("C:\\Users\\naila\\OneDrive\\Desktop\\mdp23-yolov5\\yolov5-fastapi") #change directory
RPI_IP = '192.168.23.23'
MJPEG_STREAM_URL = "http://" + RPI_IP + "/html/cam_pic_new.php"

s = socket.socket()
# host = '192.168.23.23'
host = '192.168.23.23'
port = 5001
global file_names 

print("Connecting")
s.connect((host, port))
print("Connected")

while True:
    while True:
        msg = s.recv(1024).decode()
        if msg.strip() == 'reached':
            print(msg)

            cap = cv2.VideoCapture(MJPEG_STREAM_URL)

            # Capture frame
            ret, frame = cap.read()

            if ret:
                cv2.imwrite('image.jpg', frame)

            cap.release()

            returnTest() 
            label = readID.readID()
            label = label.encode()

            img = Image.open('test.jpg')
            # img.show()

            print(label)
            s.sendall(label)
        

        # if msg.strip() == 'image':
        #     end = 'test'
        #     end = end.encode()
        #     s.sendall(end)
        #     file_names =  s.recv(1024).decode() #REPLACE THIS
        #     print("in image: " + file_names)
        #     end = 'test_1'
        #     end = end.encode()
        #     s.sendall(end)
            

        if msg.strip() == 'finish':
            # given a list = [11,12,13]
            # for each list item, iterate the folder and filenames to check for a 
            source_dir = 'C:\\Users\\naila\\OneDrive\\Desktop\\mdp23-yolov5\\yolov5-fastapi\\images'
            target_dir = 'C:\\Users\\naila\\OneDrive\\Desktop\\mdp23-yolov5\\yolov5-fastapi\\images\\to-be-stitched'

            file_names = os.listdir(source_dir)
    
            for file_name in file_names:
                if file_name.endswith('.jpg'):
                    shutil.move(os.path.join(source_dir, file_name), target_dir)
                    
            print("in stitching function")
            subprocess.run('script-imgstitch.sh', shell=True, check=True)
            print("Stitching done!") 
            end = 'done'
            end = end.encode()
            s.sendall(end)