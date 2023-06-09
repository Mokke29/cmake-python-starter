import os
import subprocess

try:
    build_path = os.path.join(os.getcwd(), "build")
    os.chdir(build_path)
    subprocess.run("cmake --build .")
    print("[info] Build finished successfully!")
except:
    print("[error] Error while building /src with (cmake --build .)")
