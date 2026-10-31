import subprocess
import os
import pyautogui
import psutil
import pathlib

result = subprocess.run(['echo', 'Hello from Emil'], capture_output=True, text=True)
print(result.stdout)