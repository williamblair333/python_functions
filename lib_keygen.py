from Crypto.PublicKey import RSA
from os import chmod

def key_generate(cipher, keyname, keypath):
    keyname = (keypath + "/" + keyname)
    keyname_public = keyname + '.pub'
        
    with open(keyname, "wb") as file_private:
        file_private.write(cipher.exportKey('PEM'))
        file_private.close()
        #chmod can't find the file unless we use explicit path
        chmod(keyname, 600)

    #start public key generation
    key_public = cipher.publickey()
    with open(keyname_public, "wb") as file_public:
        file_public.write(key_public.exportKey('OpenSSH'))
