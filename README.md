# directory-watcher-auto-formatter

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A CLI tool that watches a directory and automatically formats Python files on save using Black and isort, with Git hook integration. This helps maintain consistent code style and reduces the need for manual formatting.

## The Problem

Developers often struggle with inconsistent code style in Python projects, leading to increased maintenance costs. Current solutions require manual intervention or are too slow for large codebases. An automatic formatter that works on save can significantly improve developer productivity.

## How It Works

This tool will use file system watchers to trigger formatting on save events. It will integrate with Git hooks to ensure that only properly formatted code is committed. The core algorithm will involve parsing and rewriting Python ASTs using libraries like `ast` and `black`.

## Features

- Watches specified directories for changes and formats Python files on save.
- Integrates with Git hooks to prevent unformatted code from being committed.
- Provides configurable formatting options for Black and isort.
- Logs formatting actions to help with debugging and tracking changes.

## Installation

```bash
pip install directory-watcher-auto-formatter
```

Or install from source:

```bash
git clone https://github.com/YOUR_USERNAME/directory-watcher-auto-formatter.git
cd directory-watcher-auto-formatter
pip install -e .
```

## Quick Start

```python
# Example usage of the directory watcher
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import black
import isort

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            self.format_file(event.src_path)

    def format_file(self, path):
        with open(path, 'r+') as file:
            content = file.read()
            formatted = black.format_str(content, mode=black.FileMode())
            file.seek(0)
            file.write(formatted)
            file.truncate()

observer = Observer()
observer.schedule(ChangeHandler(), path='src/', recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
```

## Tech Stack

- `watchdog` for directory watching
- as it provides a simple API for file system events.
- `black` and `isort` for formatting and sorting imports
- ensuring code consistency.

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details.

## License

MIT License - see [LICENSE](LICENSE) for details.
