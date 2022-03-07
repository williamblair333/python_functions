import os, platform
from pathlib import Path
#################################################################################

#Get the os we're working with
os_type =  platform.platform()
os_linux = "Linux"
os_windows = "Windows"
#################################################################################

#split the keypath up to ssh directory and root directory variables
#we can start changing directories and creating the dir_ssh
#folder if it doesn't exist
def folder_split(keypath):
    if os_linux in os_type:
        dir_split = keypath.split("/")
        dir_ssh = dir_split[-1]
        del dir_split[-1]
        dir_root = ""

        for element in dir_split:
            dir_root += element + "/"

    if os_windows in os_type:
        dir_split = keypath.split("\\")
        dir_ssh = dir_split[-1]
        del dir_split[-1]
        dir_root = ""

        for element in dir_split:
            dir_root += element + "\\"

    return dir_root
#################################################################################
