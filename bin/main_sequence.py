#!/usr/bin/env python3
import os
import datetime
import subprocess

LOG_FILE = os.path.join(os.getcwd(), "logs", "system.log")

def log(message):
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{now}] {message}\n")
    print(f"[{now}] {message}")

def run_os3_pipeline():
    log("=== OS3 AUTONOMOUS SEQUENCE STARTED ===")
    
    # 1. CHECK GPS (We will mock this for now)
    log("Checking GPS for accurate UTC time... (Mock: Locked)")
    
    # 2. RUN CALIBRATION (Mock)
    log("Running star-based calibration... (Mock: [HT] Matrix generated)")
    
    # 3. CAPTURE IMAGE
    log("Executing camera capture script...")
    try:
        # This tells Python to run your capture script
        subprocess.run(["python", "bin/capture.py"], check=True)
    except subprocess.CalledProcessError:
        log("ERROR: Camera capture failed!")
        return # Stop the sequence if the camera fails

    # 4. UPLOAD IMAGE
    log("Executing upload script...")
    try:
        subprocess.run(["python", "bin/upload.py"], check=True)
    except subprocess.CalledProcessError:
        log("ERROR: Upload failed!")

    log("=== OS3 AUTONOMOUS SEQUENCE COMPLETED ===")

if __name__ == "__main__":
    run_os3_pipeline() 