import os
import shutil

file_types={'Documents':'pdf','Music':'flac','Videos':'mkv','Pictures':'jpg'}

src_dir=os.getcwd()
files=os.listdir(src_dir)

for file in files:
    for folder,ext in file_types.items():
        if file.endswith(ext):
            os.mkdir(folder)
            folder_path=os.path.join(src_dir,folder)
            shutil.move(f"{file}",folder_path)
            print(f"Moved {file} to {folder_path}")