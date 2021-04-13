import urllib.request
import requests
import numpy as np
import time
fastapi_post_url = "http://65.2.33.175:8080/predict"

imgResp=urllib.request.urlopen('file:' + r'‪C:\Users\vigne\Downloads\ezgif-frame-001.jpg')
imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8) 
start = time.time()
try:
    r = requests.post(fastapi_post_url,files={'file':imgNp})
    result=r.json()
except Exception as e:
    pass
    print("Error: ",e)
    result=None
print(result)
print("Response time: ", time.time() - start)