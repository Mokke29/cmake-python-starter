import os
import subprocess
import time
from colorama import Fore, Style
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

project_root = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../"))
main_py = os.path.join(project_root, "src", "python", "main.py")

build_root = os.path.join(project_root, "build")


class EventHandler(FileSystemEventHandler):
    main_process = None

    def on_any_event(self, event):
        # Event handler logic
        if event.is_directory:
            return
        print(event)
        process.terminate()
        self.set_main_process(None)

        subprocess.run(f"cmake --build {build_root}", shell=True)
        print(
            f"{Fore.CYAN}Event type: {event.event_type} | Path: {event.src_path}{Style.RESET_ALL}")
        print(
            f"{Fore.CYAN}[info] Restarting environment/building{Style.RESET_ALL}")

    @classmethod
    def get_main_process(cls):
        return cls.main_process

    @classmethod
    def set_main_process(cls, mp):
        cls.main_process = mp


include_dir = os.path.join(project_root, "include")
src_dir = os.path.join(project_root, "src")
print(src_dir)
# Create an event handler and observer
event_handler = EventHandler()
observer = Observer()

# Schedule the observer to watch the directory
observer.schedule(event_handler, include_dir, recursive=True)
observer.schedule(event_handler, src_dir, recursive=True)

# Start the observer
observer.start()

try:

    while True:
        if (event_handler.get_main_process() == None):
            try:
                event_handler.set_main_process(True)
                process = subprocess.Popen(["python", main_py], shell=True)
            except:
                event_handler.set_main_process(True)
                process = subprocess.Popen(["python3", main_py], shell=True)
        time.sleep(1)
except KeyboardInterrupt:
    # Stop the observer if Ctrl+C is pressed
    observer.stop()

# Wait for the observer to complete
observer.join()
