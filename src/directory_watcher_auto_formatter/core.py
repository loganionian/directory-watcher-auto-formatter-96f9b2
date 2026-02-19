import os
import time
import black
import isort
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            self.format_file(event.src_path)

    def format_file(self, path: str) -> None:
        """Formats a Python file using Black and isort."""
        try:
            with open(path, 'r+') as file:
                content = file.read()
                # Format with isort first to sort imports
                sorted_content = isort.code(content)
                # Then format with Black for consistent style
                formatted_content = black.format_str(sorted_content, mode=black.FileMode())
                file.seek(0)
                file.write(formatted_content)
                file.truncate()
        except Exception as e:
            print(f"Error formatting file {path}: {e}")

def start_watching(path: str) -> None:
    """Starts the directory watcher."""
    observer = Observer()
    observer.schedule(ChangeHandler(), path=path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()