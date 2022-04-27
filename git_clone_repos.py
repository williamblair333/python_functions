
################################################################################
#Modified from: https://stackoverflow.com/questions/19576742/how-to-clone-all-repos-at-once-from-github
# Martin Thoma, May 2020
#
#READ THE COMMENTS BEFORE RUNNING
#Run:	    python3 -m git_clone_repos -u "username" 
#File:      git_clone_repos.py
#Date:      2022APR18
#Author:    William Blair
#Contact:   williamblair333@gmail.com
#Tested on: Windows 10 21H1 
#
#This script is intended to do the following:
#
#-git clone all repos belonging to username.
#-Will clone private repos if users is already authenticated, otherwise public
#-TODO:  None yet
#-REF: https://developer.github.com/v3/repos/#list-repositories-for-a-user

################################################################################

import urllib.request, base64
import json
import os
import argparse

parser = argparse.ArgumentParser(description='Github clone all repos')
parser.add_argument('-u', '--username', \
type=str, help='Enter the Github org or username here' + \
'username,\t Required', required=True)

args = parser.parse_args()
username = (args.username)

def get_urls(username):
    url = f"https://api.github.com/users/{username}/repos?per_page=200"
    request = urllib.request.Request(url)
    result = urllib.request.urlopen(request)
    return json.load(result)

if __name__ == "__main__":
    for link in get_urls(username):
        if not os.path.isdir(link["name"]):
            print(f"Clone {link['name']}...")
            os.system("git clone " + link["ssh_url"])
        else:
            print(f"SKIP {link['name']}...")