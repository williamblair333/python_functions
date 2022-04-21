################################################################################
#
#READ THE COMMENTS BEFORE RUNNING
#Run:	    python3 -m repo-venv-install-git
#File:      repo-venv-install-git.py
#Date:      2022APR18
#Author:    William Blair
#Contact:   williamblair333@gmail.com
#Tested on: Debian 11 && Windows 10 21H2
#
#This script is intended to do the following:
#-Automatically a git repo and setup a .venv under home directory
#-TODO args to: specify venv folder location, repo
#-TODO function to make get clone or venv setup optional
#-TODO cleanup and 'professionalize'
################################################################################

import os
import platform
from pathlib import Path
from subprocess import call
import sys
#################################################################################

dir_home = str(Path.home())
os_type =  platform.platform()
os_ver = platform.version()
os_linux = "Linux"
os_windows = "Windows"
#################################################################################

git_server = "192.168.1.10"
repo_get = 'git clone https://' + git_server + ':/user/repo.git'
#################################################################################

py_ver_long = sys.version
py_ver_num = py_ver_long.split()
py_ver_num = "python" + py_ver_num[0][0:3]
#py_ver_num = py_ver_num[0]
#################################################################################

#pip && pipenv setup && execution
pip_pipenv_install = 'pip install pipenv'
pip_upgrade_user = 'pip install --upgrade --user pip'
pip_upgrade_system = 'pip install --upgrade pip'
pip_packages = "curl -o requirements.txt http://" + git_server + \
    ":user/repo/raw/branch/main/requirements.txt"

venv_home = '.venv'
pipenv_setup = 'mkdir ' + venv_home + '&& cd .venv'
#################################################################################

def webdriver_install():
    driver_chrome = 'webdrivermanager chrome -l AUTO'
    driver_firefox = 'webdrivermanager firefox -l AUTO'
#################################################################################

if os_linux in os_type:
    pipenv_installer = '$HOME/.local/bin/pipenv install'

    os.system(repo_get)

    set_py_path = 'export PATH=$PATH:/usr/local/bin/python'

    set_web_path = 'export PATH=$PATH:' + dir_home + \
                   '/.local/share/WebDriverManager/bin'

    set_bin_path = 'echo export PATH=$PATH:' + dir_home + \
                   '/.local/bin >>' + dir_home + '/.bashrc'

    #run all the commands together in one sub-process
    os.system(('cd "$HOME"; ') + \
              set_py_path + "; " + \
              set_web_path + "; " + \
              set_bin_path + "; " + \
              pip_pipenv_install + "; " + \
              pip_upgrade_user + "; " + \
              pip_upgrade_system + "; " + \
              pip_packages + "; " + \
              pipenv_setup + "; " + \
              pipenv_installer + "; " + \
              py_utils)

    webdriver_install()
#################################################################################

if os_windows in os_type:
    pipenv_installer = 'pipenv install'

    os.system(repo_get)

    #run all the commands together in one sub-process
    os.system(('cd %USERPROFILE% ') + " & " + \
              'python3 -m ' + pip_pipenv_install + " & " + \
              'python3 -m ' + pip_upgrade_user + " & " + \
              'python3 -m ' + pip_upgrade_system + " & " + \
              'python3 -m ' + pip_packages + " & " + \
              pipenv_setup + " & " + \
              'python3 -m ' + pipenv_installer + " & " + \
              py_utils)

    webdriver_install()
#################################################################################
