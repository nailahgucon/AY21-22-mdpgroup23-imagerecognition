from cv2 import randShuffle
from fastapi import FastAPI, File
from segmentation import get_yolov5, get_image_from_bytes
from starlette.responses import Response
import io
from PIL import Image
import json
from fastapi.middleware.cors import CORSMiddleware
import cv2

count = 0
model = get_yolov5()

app = FastAPI(
    title="Custom YOLOV5 Machine Learning API",
    description="""Obtain object value out of image
                    and return image and json result""",
    version="0.0.1",
)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/object-to-json")
async def detect_return_json_result(file: bytes = File(...)):
    input_image = get_image_from_bytes(file)
    results = model(input_image)
    detect_res = results.pandas().xyxy[0].to_json(orient="records")  # JSON img1 predictions
    detect_res = json.loads(detect_res)

    checker = 0
    for i in range(0,len(detect_res)):
        if detect_res[i]["class"] != 41: # 41 is the ID of bullseye
            with open('TEST.txt', 'w') as f:
                f.write(str(detect_res[i]["class"]))
            checker = 1
            break
    
    if checker == 0:
        with open('TEST.txt', 'w') as f:
                f.write(str(0))

    return {"result": detect_res}


@app.post("/object-to-img")
async def detect_return_base64_img(file: bytes = File(...)):
    global count
    output_path = './images/'
    input_image = get_image_from_bytes(file)
    results = model(input_image)
    results.render()  # updates results.imgs with boxes and labels
    for img in results.imgs:
        bytes_io = io.BytesIO()
        img_base64 = Image.fromarray(img)
        img_base64.save(bytes_io, format="jpeg")

    with open("TEST.txt", "r") as fp:
        lines = fp.readlines()
        first = lines[0]
    
    if first != "0":
        #cv2.imwrite(output_path + 'detection' + str(count) + '.jpg', img)
        cv2.imwrite(output_path + first + '.jpg', img)
        count = count + 1

    return Response(content=bytes_io.getvalue(), media_type="image/jpeg")
