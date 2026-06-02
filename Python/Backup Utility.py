import shutil
import os

def backup_files(files, backup_folder):
    copied = set()

    os.makedirs(backup_folder, exist_ok=True)

    with open("backup.log", "a") as log:

        for file in files:
            try:
                filename = os.path.basename(file)

                if filename in copied:
                    continue

                shutil.copy(file, backup_folder)

                copied.add(filename)

                log.write(f"Copied: {filename}\n")

            except FileNotFoundError:
                log.write(f"Not Found: {file}\n")

            except PermissionError:
                log.write(f"Permission Denied: {file}\n")

files = ["sample1.txt", "sample2.txt"]

backup_files(files, "backup")