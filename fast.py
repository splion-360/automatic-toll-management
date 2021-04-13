import numpy as np
import sys, os
from fastapi import FastAPI, UploadFile, File
from starlette.requests import Request
import io
import cv2
import subprocess
from pydantic import BaseModel
import uvicorn

app = FastAPI()
class ImageType(BaseModel):
    url: str
@app.get("/")
def home():
    return "Home"
@app.post("/predict/") 
def prediction(request: Request, file: bytes = File(...)):
    if request.method == "POST":
        image_stream = io.BytesIO(file)
        image_stream.seek(0)
        file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
        frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        cv2.imwrite("carlp.jpg", frame)
        string_cmd = "docker run --rm -v"+os.path.dirname(os.getcwd())+":/workspace -w /workspace daisukekobayashi/darknet:cpu-cv darknet detector test lp.data license-plate.cfg license-plate_final.weights -i 0 -thresh 0.25 carlp.jpg -ext_output"
        cmd = string_cmd.split(" ")
        result = subprocess.run(cmd, capture_output=True).stdout.decode('utf-8')
        result_json = {}
        obj_id = 0
        for i in enumerate(result.splitlines()):
            if i.startswith("LP"):
                    result_json[obj_id] = i
                    obj_id +=1
        return result_json
    return "No post request found"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)