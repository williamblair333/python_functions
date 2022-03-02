################################################################################
#
#READ THE COMMENTS BEFORE RUNNING
#Run:        python3 -m ssh_keygen
#File:       ssh_keygen.py
#Date:       2022FEB02
#Author:     William Blair
#Contact:	   williamblair333@gmail.com
#Tested on:  Debian 11, Windows 10 21H1
#
#This script intends to do the following:
#
#- Generate ssh public and private keys compatible with Linux and hopefully
#- other operating systems
#- TODO
#- Make a function out of it for custom file names, paths, and whatnot
################################################################################

'''
Old crypto libraries will cause problems
python3 -m pip uninstall crypto 
python3 -m pip uninstall pycrypto 
python3 -m pip install pycryptodome
'''
#################################################################################

from Crypto.PublicKey import RSA
from pathlib import Path
from os import chmod

keyname_private = "id_rsa"
keyname_public = keyname_private + '.pub'
#sets a path variable
pwd = Path.cwd()

cipher_strength = 2048
cipher = RSA.generate(cipher_strength)

#start private key generation
with open(keyname_private, "wb") as file_private:
    file_private.write(cipher.exportKey('PEM'))
    file_private.close()
    #chmod can't find the file unless we use explicit path
    keyname_private = (pwd / keyname_private)
    chmod(keyname_private, 600)
    print(keyname_private)

#start public key generation
key_public = cipher.publickey()
with open(keyname_public, "wb") as file_public:
    file_public.write(key_public.exportKey('OpenSSH'))
    print(keyname_public)
