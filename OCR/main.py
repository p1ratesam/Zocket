from fastapi import FastAPI, File, UploadFile
from typing import List
import time
import asyncio
import ocr
import re
import utils

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Visit the endpoint: /api/v1/extract_text to perform OCR."}

@app.post("/api/v1/extract_text")
async def extract_text(Images: List[UploadFile] = File(...)):
    response = {}
    s = time.time()
    for img in Images:
        print("Images Uploaded: ", img.filename)
        temp_file = utils._save_file_to_server(img, path="./", save_as=img.filename)
        text = await ocr.read_image(temp_file)

        name = re.findall(r'Name : (.*)',text)
        emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
        phone_no = re.findall(r' Phone : (.*)',text)
        address = re.findall(r'Address : (.*)',text)

        # name = re.findall("(Name : [\w]+[\s]+[\w])",text)
        response["Name"] = name
        response["Phone"] = phone_no
        response["E-mail"] = emails
        response["Address"] = address
    response["Time Taken"] = round((time.time() - s),2)

    return response
