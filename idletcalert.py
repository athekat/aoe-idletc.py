import pyautogui
import time
from playsound import playsound
import sys
import os

ICON_IMAGE_PATH = 'malevil.png'  
SOUND_FILE_PATH = os.path.dirname(__file__) + '\\alert.wav'   
REGION_TO_SEARCH = (0, 0, 310, 160) 
CONFIDENCE_LEVEL = 0.6 
CHECK_INTERVAL_SECONDS = 3

print("Starting in 5 seconds...")
time.sleep(5)
try:
    while True:
        try:
            if REGION_TO_SEARCH:
                icon_location = pyautogui.locateOnScreen(
                    ICON_IMAGE_PATH, grayscale=True,
                    region=REGION_TO_SEARCH,
                    confidence=CONFIDENCE_LEVEL
                )
            else:
                icon_location = pyautogui.locateOnScreen(
                    ICON_IMAGE_PATH,
                    confidence=CONFIDENCE_LEVEL
                )

            if icon_location:
                print(f"[{time.strftime('%H:%M:%S')}] Good, you're making vils.")
            else:
                print(f"[{time.strftime('%H:%M:%S')}] Icon NOT found! Playing sound...")
                try:
                    playsound(SOUND_FILE_PATH)
                    print("Sound played.")
                except Exception as e:
                    print(f"Error playing sound: {e}")
                    print("Ensure 'playsound' is installed and the sound file path is correct and accessible.")

        except pyautogui.PyAutoGUIException as e:
            print(f"[{time.strftime('%H:%M:%S')}] You're not making vils, playing sound alert.")
            # pyautogui.press('3') # Go to TC
            # pyautogui.press('c') # Make a vil
            playsound(SOUND_FILE_PATH)
        except FileNotFoundError as e:
            print(f"[{time.strftime('%H:%M:%S')}] File not found error: {e}")
            print("Please ensure ICON_IMAGE_PATH and SOUND_FILE_PATH are correct.")
        except Exception as e:
            print(f"[{time.strftime('%H:%M:%S')}] An unexpected error occurred: {e}")

        # Wait before the next check
        time.sleep(CHECK_INTERVAL_SECONDS)

except KeyboardInterrupt:
    print("\nScript stopped by user (Ctrl+C). Exiting.")
    sys.exit(0) # Exit cleanly