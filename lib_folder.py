import os
from pathlib import Path

def folder_create(path_ssh, dir_ssh, dir_home):
    if os.path.exists(path_ssh):
        print(f'Folder "{dir_ssh}" exist!')
    else:
        os.chdir(dir_home)
        os.mkdir(dir_ssh)
        print(f'Folder "{dir_ssh}" succesfully created!')
        return


