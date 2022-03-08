#################################################################################
#
#READ THE COMMENTS BEFORE RUNNING
#Run:        python3 ssh_keygen.py -b 4096 -k my_id_rsa -p /home/user/.ssh
#Run:        python3 ssh_keygen.py -b 4096 -k my_id_rsa -p C:\users\winuser\.ssh
#File:       ssh_keygen.py
#Date:       2022FEB02, updated 2022MAR07
#Author:     William Blair
#Contact:	 williamblair333@gmail.com
#Tested on:  Debian 11, Windows 10 21H2,
#
#This script intends to do the following:
#
#- Generate ssh public and private keys compatible with Linux and hopefully
#- other operating systems.
#- TODO
#- Error handling..
#################################################################################
'''
Old crypto libraries will cause problems. Run this..
python3 -m pip uninstall crypto 
python3 -m pip uninstall pycrypto 
python3 -m pip install pycryptodome
'''
#################################################################################

import lib_keygen as ssh
#import argparse, csv, os, platform, sys, time
import argparse, os, platform
#from subprocess import call
from Crypto.PublicKey import RSA
from pathlib import Path
#from os import chmod
#################################################################################

#OS handling will go here.. function coming?
os_type =  platform.platform()
os_ver = platform.version()
os_linux = "Linux"
os_windows = "Windows"
#################################################################################

#Setting for variables for default arguments
dir_home = str(Path.home())
dir_ssh = ".ssh"
#################################################################################

#Setting up arguments and defaults
#Notes:  
#    default is the value that the attribute gets when the argument is absent. 
#    const is the value it gets when given. 
#    const is allowed only when the action is store_const
parser = argparse.ArgumentParser(description='To set ssh key bit size, name ' + \
'and path location.')

parser.add_argument('-b', '--bits', type=str, nargs='?', default="2048", \
help='SSH key bit strength. Default is 2048.', required=False)

parser.add_argument('-k', '--keyname',   type=str, nargs='?', default="id_rsa", \
help='Private key name. Default name is id_rsa.', required=False)

if os_linux in os_type:
    #path_ssh = dir_home + "/" + dir_ssh
    parser.add_argument('-p', '--keypath', \
    type=str, nargs='?', \
    default=dir_home + "/" + dir_ssh, \
    help='Key folder path location.  Default path is $HOME/.ssh.', \
    required=False)

if os_windows in os_type:
    path_ssh = dir_home + "\\" + dir_ssh
    parser.add_argument('-p', '--keypath', \
    type=str, nargs='?', \
    default=dir_home + "\\" + dir_ssh, \
    help='Key folder path location.  Default path is %USERPROFILE%\.ssh.', \
    required=False)

args = parser.parse_args()
bits  = (args.bits)
keyname = (args.keyname)
keypath = (args.keypath)
#################################################################################

if not os.path.exists(keypath):
    try:
        os.makedirs(keypath)
    except PermissionError:
        print("Permission denied creating a folder here, exiting.")
else:
    os.chdir(keypath)
#################################################################################

#start private & public key generation
if os.path.exists(keyname):
    print("SSH key exists! Terminating program!")
    quit()

cipher = RSA.generate(int(bits))
ssh.key_generate(cipher, keyname, keypath)
#################################################################################
