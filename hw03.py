import os
import sys
from pathlib import Path
from colorama import Fore, Style

def visualize_directory(path: Path, indent: str = ""):
    if not path.is_dir():
        print(f"{path} is not directory")
        return

    for entry in os.listdir(path):
        full_path = path / entry
        if full_path.is_dir():
            print(f"{indent}{Fore.BLUE}{entry}/{Style.RESET_ALL}")
            visualize_directory(full_path, indent + "  ")
        else:
            print(f"{indent}{Fore.GREEN}{entry}{Style.RESET_ALL}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Using: python hw03.py <path to directory>")
        sys.exit(1)

    directory_path = Path(sys.argv[1])
    visualize_directory(directory_path)
