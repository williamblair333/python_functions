################################################################################
#
#READ THE COMMENTS BEFORE RUNNING
#Run:        python3 ssh_keygen.py -b 4096 -k my_id_rsa -p /home/user/dir1/subdir1/subdir2/.ssh
#File:       ssh_keygen.py
#Date:       2022FEB02
#Author:     William Blair
#Contact:	 williamblair333@gmail.com
#Tested on:  Debian 11
#
#This script intends to do the following:
#
#- Generate ssh public and private keys compatible with Linux and hopefully
#- other operating systems.
#- TODO
#- Make a function out of it for custom key type, strengths,
#- file names, paths, and whatnot.
#- Differentiate between OS versions
#- Error handling..
################################################################################

'''
Old crypto libraries will cause problems. Run this..
python3 -m pip uninstall crypto 
python3 -m pip uninstall pycrypto 
python3 -m pip install pycryptodome
'''
#################################################################################
import lib_folder
import lib_os
import argparse, csv, os, platform, sys, time
from subprocess import call
from Crypto.PublicKey import RSA
from pathlib import Path
from os import chmod
#################################################################################

#Setting for variables for default arguments
dir_home = str(Path.home())
dir_ssh = ".ssh"
path_ssh = dir_home + "/" + dir_ssh

#Setting up arguments and defaults
parser = argparse.ArgumentParser(description='To set ssh key bit size, name ' + \
'and path location.')

parser.add_argument('-b', '--bits', type=str, nargs='?', const="2048", \
help='SSH key bit strength. Default is 2048.', required=False)

parser.add_argument('-k', '--keyname',   type=str, nargs='?', const="id_rsa", \
help='Private key name. Default name is id_rsa.', required=False)

parser.add_argument('-p', '--keypath',   type=str, nargs='?', const=path_ssh, \
help='Private and public key folder path location.  Default path is ${HOME}/.ssh.', \
required=False)

args = parser.parse_args()
bits  = (args.bits)
keyname = (args.keyname)
keypath = (args.keypath)
#################################################################################

#OS handling will go here.. function coming?
os_type =  platform.platform()
os_linux = "Linux"
os_windows = "Windows"

'''
if os_windows in os_type:
    print("This is windows")
    parser.add_argument('-p', '--keypath', type=str, nargs='?', const="%USERPROFILE%\.ssh", \
    help='Private and public key folder path location.  Default path is ${HOME}/.ssh.', \
    required=False)
else:
    print("This is...")

#keyname = "id_rsa"
#sets a path variable
#keypath = Path.cwd()
#bits = 2048
'''
#################################################################################

#split the keypath up to ssh directory and root directory variables
#we can start changing directories and creating the dir_ssh
#folder if it doesn't exist
dir_split = keypath.split("/")
dir_ssh = dir_split[-1]
del dir_split[-1]
dir_root = ""

for element in dir_split:
    dir_root += element + "/"

#create the .ssh folder if it doesn't exist
lib_folder.folder_create(keypath, dir_ssh, dir_root)
os.chdir(keypath)
#################################################################################

#start private key generation
keyname_public = keyname + '.pub'
cipher = RSA.generate(int(bits))

with open(keyname, "wb") as file_private:
    file_private.write(cipher.exportKey('PEM'))
    file_private.close()
    #chmod can't find the file unless we use explicit path
    keyname = (keypath + "/" + keyname)
    print(keyname)
    chmod(keyname, 600)

#start public key generation
key_public = cipher.publickey()
with open(keyname_public, "wb") as file_public:
    file_public.write(key_public.exportKey('OpenSSH'))
