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

#Create Folder if don't exist
for folder in file_types.keys():
        folder_path = os.path.join(src_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            
for file in os.listdir(src_dir):
    file_path=os.path.join(src_dir,file)
    if os.path.isfile(file_path):
        _, file_ext=os.path.splitext(file)
        
        # To find the appropriate Folder
        destination_folder='Others'
        for folder,ext in file_types.items():
            if file_ext in ext:
                destination_folder=folder
                break
            
        dst_path=os.path.join(src_dir,destination_folder)
        shutil.move(f"{file}",dst_path)
        print(f"Moved {file} to {dst_path}")