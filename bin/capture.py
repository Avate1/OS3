#!/usr/bin/env python3
import time
import os
import datetime
import json

BASE_DIR = os.getcwd()
IMAGE_DIR = os.path.join(BASE_DIR, "images")
LOG_FILE = os.path.join(BASE_DIR, "logs", "camera.log")

# Safety check: create folders if they don't exist
os.makedirs(IMAGE_DIR, exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "logs"), exist_ok=True)

def capture():
    now = datetime.datetime.now(datetime.timezone.utc)
    time_string = now.strftime("%Y%m%dT%H%M%SZ")
    filename = f"RSO_{time_string}.jpg"
    image_path = os.path.join(IMAGE_DIR, filename)
    
    print(f"--- OS3 CAMERA TRIGGERED ---")
    
    # --- REAL HARDWARE STUB ---
    # When the Canon/Nikon camera arrives, you will uncomment this line:
    # os.system(f"gphoto2 --capture-image-and-download --filename {image_path}")
    
    # --- MOCK HARDWARE (Current) ---
    time.sleep(2)
    with open(image_path, "w") as f:
        f.write("THIS IS A FAKE IMAGE")
    
    print(f"Success! Created image: {image_path}")
    
if __name__ == "__main__":
    capture()