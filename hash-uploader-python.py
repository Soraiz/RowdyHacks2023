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
    
    def analyze(self):
        print (Net_Colors.BLUE + " collect info/data about the results of the analysis...." + Net_Colors.ENDC)
        analysis_url = VT_API_URL + "analyses/" + self.headers)
        reswr = requests.get("data").get("attributes").get("stats")
        
    
        
        
        
    