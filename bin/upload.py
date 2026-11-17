#!/usr/bin/env python3
import os
import shutil
import glob
import datetime

BASE_DIR = os.getcwd()
IMAGE_DIR = os.path.join(BASE_DIR, "images")
UPLOAD_DIR = os.path.join(BASE_DIR, "uploaded")
LOG_FILE = os.path.join(BASE_DIR, "logs", "upload.log")

def upload():
    now = datetime.datetime.now(datetime.timezone.utc)
    time_string = now.strftime("%Y%m%dT%H%M%SZ")
    
    files = glob.glob(os.path.join(IMAGE_DIR, "*"))
    
    with open(LOG_FILE, "a") as f:
        f.write(f"[{time_string}] Found {len(files)} files to upload.\n")

    for file in files:
        filename = os.path.basename(file)
        shutil.move(file, os.path.join(UPLOAD_DIR, filename))
        
        with open(LOG_FILE, "a") as f:
            f.write(f"[{time_string}] Uploaded: {filename}\n")

if __name__ == "__main__":
    upload()