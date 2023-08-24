from .dependencies import os

#get directory path
project_dir = os.getcwd()

##########################

#creat Image folder path
DEFAULT_FOLDER_PATH  = os.path.join(project_dir, 'Images/')
is_exist = os.path.exists(DEFAULT_FOLDER_PATH)
if not is_exist:
    os.mkdir(DEFAULT_FOLDER_PATH)  

