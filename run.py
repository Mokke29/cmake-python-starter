import os
import subprocess
import sys

dev_py = os.path.join(os.getcwd(), "tools", "watching.py")
main_py = os.path.join(os.getcwd(),  "src", "python", "main.py")

if len(sys.argv) < 2:
    try:
        subprocess.run(f"python {main_py}", shell=True)
    except:
        subprocess.run(f"python3 {main_py}", shell=True)
else:
    if (sys.argv[1] == "dev"):
        try:
            subprocess.run(f"python {dev_py}", shell=True)
        except:
            subprocess.run(f"python3 {dev_py}", shell=True)
