import os 
import sys 
import time 
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ScriptHandler(FileSystemEventHandler):

    def __init__(self, script_path, args):
        self.script_path = script_path
        self.args = args 
        self.process = None 
        self.start_script()

    def start_script(self):
        if self.process:
            self.process.terminate()
            self.process.wait()
        print(f'Starting script: {self.script_path}')
        self.process = subprocess.Popen([sys.executable, self.script_path] + self.args)

    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f'Detected change in {event.src_path}. Restarting script...')
            self.start_script()

def track_script(script_path, args=[]):
    if not os.path.isfile(script_path):
        print(f'Error: The file {script_path} does not exist.')
        return 

    script_handler = ScriptHandler(script_path=script_path, args=args)
    observer = Observer()
    observer.schedule(script_handler, path=os.path.dirname(script_path), recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python main.py <script_path> [args...]')
        sys.exit(1)
    
    script_path = os.path.abspath(sys.argv[1])
    args = sys.argv[2:]
    track_script(script_path, args)

