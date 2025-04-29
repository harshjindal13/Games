# don't forget to uncomment the line number: 32, 41

import random
import time
import sys
import os

def print_progress_bar(duration):
    
    for i in range(1, 101):
        sys.stdout.write(f"\rDownloading package... {i}%")
        sys.stdout.flush()
        time.sleep(duration / 100)
    print("\n")

if random.randint(0, 6) == 1:
    print("Initiating advanced memory bypass...")
    time.sleep(1)
    print("Warning: Critical system process detected. Attempting to bypass memory safeguards...")
    time.sleep(2)

    
    print_progress_bar(5)  # Simulate a 5-second "download"

    print("Memory wipe in progress...")
    print_progress_bar(10)  # Simulate a 10-second memory wipe "download"

    print("\nWARNING: Attempting to remove system files...")
    time.sleep(2)
    
    
    # os.remove("C:\\Windows\\System32") 

    print("os.remove('C:\\Windows\\System32')")  # Just showing as a comment
    time.sleep(1)
    
    print("Deleting system files... 😈")
    time.sleep(3)

   
    # os.remove("C:\\Windows\\System32")  

    print("Memory wiped!")
    time.sleep(1)
    print("System rebooting...")
    time.sleep(2)

    print("Just kidding! Your memory is safe. Focus on your own progress instead of mocking others.")
else:
    print("System is running smoothly.")
