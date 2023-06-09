import os
import subprocess

main_py = os.path.join(os.getcwd(), "src", "python", "main.py")

try:
    subprocess.run(f"python {main_py}")
except:
    subprocess.run(f"python3 {main_py}")
