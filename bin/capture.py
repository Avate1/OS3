#!/usr/bin/env python3
import time
import os
import datetime
import json

# This gets the folder you are currently running the script from
BASE_DIR = os.getcwd() 
IMAGE_DIR = os.path.join(BASE_DIR, "images")
LOG_FILE = os.path.join(BASE_DIR, "logs", "camera.log")

def capture():
    now = datetime.datetime.now(datetime.timezone.utc)
    time_string = now.strftime("%Y%m%dT%H%M%SZ")
    filename = f"RSO_{time_string}.jpg"
    
    with open(LOG_FILE, "a") as f:
        f.write(f"[{time_string}] Camera triggered. Simulating 2 second exposure...\n")
    
    # Wait 2 seconds to simulate exposure
    time.sleep(2)
    
    # Create a fake image
    with open(os.path.join(IMAGE_DIR, filename), "w") as f:
        f.write("THIS IS A FAKE IMAGE")
        
    with open(LOG_FILE, "a") as f:
        f.write(f"[{time_string}] Success! Saved {filename}\n")

    # Create JSON manifest
    manifest = {"image_name": filename, "utc_time": time_string}
    with open(os.path.join(IMAGE_DIR, f"manifest_{time_string}.json"), "w") as f:
        json.dump(manifest, f, indent=4)

if __name__ == "__main__":
    capture()