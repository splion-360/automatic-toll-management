#-- coding: utf-8 --
import os
import urllib.request
import requests
import numpy as np
import time
import boto3
from dotenv import load_dotenv

load_dotenv()

# CONNECTION TO API
ACCESS_ID = os.getenv("ACCESS_ID")
ACCESS_KEY = os.getenv("ACCESS_KEY")
ec2 = boto3.client('ec2',region_name='ap-south-1', aws_access_key_id=ACCESS_ID,
         aws_secret_access_key= ACCESS_KEY)
response = ec2.describe_instances()
if response["Reservations"][0].get(u"Instances")[0].get(u"PublicIpAddress") is not None:
    ip_address = response["Reservations"][0].get(u"Instances")[0].get(u"PublicIpAddress")
else:
    print("Unable to get instance IP address")

fastapi_post_url = f"http://{ip_address}:8080/predict"

# POSTING LOCAL IMAGE
imgResp=urllib.request.urlopen('file:' + r"C:\Users\vigne\Desktop\automatic-toll-management\test_images\2.jpg") # IMAGE PATH HERE
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