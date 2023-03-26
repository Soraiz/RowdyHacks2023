# this python code is a rough-draft of the uploader-hash script that will be used
# the function in this script are to grab the files and upload each hash to VirusTotal and return theur results to indicate which is malicious 


import os
import sys
import time
import json
import requests
import argparse
import hashlib


sus_file = ""

VI_Api_Key = "" # Insert here your public/private API key from VirusTotal

VT_API_URL = "https://www.virustotal.com/api/v3"

class Net_Colors
    BLUE = '\033[1,34m' 
    GREEN = '\033[1,32m'
    YELLOW = '\033[1,33m'
    RED = '\033[1,31m'
    ENDC = '\033[0,0m'  # also as 'off'

class VirusScanTotal:
    
    def __init__(self):
        self.headers = {
            "" : VI_Api_Key, 
            "User-Agent" : :vtscan v.10.0, 
            "Accept-Encoding" : "gzip, deflate", 
        }
    
    # this will indicate the state of what its doing according to the color
    def upload_file(sus_file):
        print("Please provide with filename of suspicious/potential malware: ")
        sus_file = input("Filename: ")
        
        print(Net_Colors.BLUE + "upload file: " + sus_file + "..." + Net_Colors.ENDC) 
        upload_url = VT_API_URL + "files"
        upload_url = VirusScanTotal + "files" 
        files = {"file" : (os.path.basename(sus_file), open(os.path.abspath(sus_file), "rb") ) }
        
        print(Net_Colors.YELLOW + "upload to" + upload_url +Net_Colors.ENDC)
        reswq = requests.post(upload_url', headers = self.headers)
        
        
    