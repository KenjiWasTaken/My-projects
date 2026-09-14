import os
import shutil

folders = {
    ".jpg": "Images",
    ".png": "Images",
    ".mp3": "Music",
}

def organize_file(file):
    if not os.path.isfile(file):
        return None

    name, extension = os.path.splitext(file)

    destination = os.path.join(folder, file)

    if os.path.exists(destination):
        return None

    if extension in folders:
        folder = folders[extension]
        shutil.move(file, folder)
        return folder

    return None

for folder in folders.values():
    if not os.path.exists(folder):
        os.mkdir(folder)

files = os.listdir(".")

for file in files:
    destination = organize_file(file)

    if destination:
        print(f"Moved {file} to {destination}/")
        print(f"Successfully organized into {destination}/")
    
    else:
        print(f"{file} was not organized/")