import shutil
from pathlib import Path

folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "Music": [".mp3", ".wav", ".flac", ".ogg", ".m4a"],
    "Documents": [".pdf", ".doc", ".docx", ".odt", ".txt", ".rtf"],
    "Spreadsheets": [".xls", ".xlsx", ".csv", ".ods"],
    "Archives": [".zip", ".7z", ".rar", ".tar", ".gz", ".bz2", ".xz"],
    "Programs": [".deb", ".AppImage", ".exe", ".msi"],
    "Code": [".py", ".c", ".h", ".cpp", ".js", ".html", ".css", ".sh"]
}

def create_folder(extension, folder_name, folder_extensions):
    if extension in folder_extensions:
        folder = Path(folder_name)
        if not folder.exists():
            folder.mkdir()

def find_destination(file: Path):
    file_extension = file.suffix
    file_extension = file_extension.lower()


    for folder_name, folder_extensions in folders.items():
        if file_extension in folder_extensions:
            create_folder(file_extension, folder_name, folder_extensions)
            if move(file, folder_name):
                return folder_name

    print(f"{file.name} not moved!")

def move(file, folder):
    folder = Path(folder)
    file = Path(file)
    destination = folder / file.name
    
    if destination.exists():
        print(f"Cannot move {file}!\nFilename is occupied!")
        return False

    shutil.move(file, destination)
    print(f"Moved {file} to {folder}")
    return True

directory = Path()

for file in directory.iterdir():    
    if file.is_file():
        destination = find_destination(file)    