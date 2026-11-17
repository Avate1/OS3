#!/usr/bin/env python3
import os
import shutil
import glob
import datetime

BASE_DIR = os.getcwd()
IMAGE_DIR = os.path.join(BASE_DIR, "images")
UPLOAD_DIR = os.path.join(BASE_DIR, "uploaded")
LOG_FILE = os.path.join(BASE_DIR, "logs", "upload.log")

os.makedirs(UPLOAD_DIR, exist_ok=True)

def upload():
    now = datetime.datetime.now(datetime.timezone.utc)
    time_string = now.strftime("%Y%m%dT%H%M%SZ")
    
    print(f"--- OS3 UPLOADER MOCK STARTED ---")
    print(f"Scanning folder: {IMAGE_DIR}")
    
    files = glob.glob(os.path.join(IMAGE_DIR, "*"))
    print(f"Found {len(files)} files to upload.")
    
    with open(LOG_FILE, "a") as f:
        f.write(f"[{time_string}] Found {len(files)} files to upload.\n")

    if len(files) == 0:
        print("Nothing to upload. Exiting.")

    for file in files:
        filename = os.path.basename(file)
        dest_path = os.path.join(UPLOAD_DIR, filename)
        
        shutil.move(file, dest_path)
        
        print(f"Moved {filename} to {UPLOAD_DIR}")
        
        with open(LOG_FILE, "a") as f:
            f.write(f"[{time_string}] Uploaded: {filename}\n")
            
    print(f"--- UPLOADER MOCK FINISHED ---")

if __name__ == "__main__":
    upload()