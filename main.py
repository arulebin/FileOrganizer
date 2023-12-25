import os
import shutil

file_types={
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
        'Music': ['.mp3', '.wav', '.flac'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Others':[]
    }

src_dir=os.getcwd()

for file in os.listdir(src_dir):
    _, file_ext=os.path.splitext(file) 
    
    for folder,ext in file_types.items():  
        if file_ext in ext:
            os.mkdir(folder)
            folder_path=os.path.join(src_dir,folder)
            shutil.move(f"{file}",folder_path)
            print(f"Moved {file} to {folder_path}")