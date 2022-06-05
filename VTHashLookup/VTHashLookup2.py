#Detection Logic:
# open file
# read file
#go to vti and lookup the hash
# get the hash values from virustotal and write them to another file
#loop until all hashes are done

#Under Progress notes:
#try to get support for multiple inputfile types like txt, csv and xlsx. makes it easier to use
# try to also add the malware bazaar and anomali threat stream api for hash lookup as well
#clean up this script, create functions to section out the code


import json
import requests
import csv
import os
from dotenv import load_dotenv
load_dotenv()



inputFile=os.getenv("HOME")+"test.csv"
outputFile=os.getenv("HOME")+"output.csv"


headers = {
    "Accept": "application/json",
    "x-apikey": os.getenv("api_key_vti")
}

csvheader=['MD5','SHA1','SHA256']


with open(inputFile)as csvfile:
    csvreader=csv.reader(csvfile)
    with open(outputFile, "w",newline= '')as file:
        csvwriter=csv.writer(file)
        csvwriter.writerow(csvheader)
    for row in csvreader:
        HASH=""
        for char in row:
            HASH+=char
        #print(HASH)
        url = f"https://www.virustotal.com/api/v3/files/{HASH}"
        #print(url)
        response = requests.request("GET", url, headers=headers, verify = False)
        if response.status_code==200:
            x= json.loads(response.text)
            md5=(x["data"]["attributes"]["md5"])
            sha1=(x["data"]["attributes"]["sha1"])
            sha256=(x["data"]["attributes"]["sha256"])
            print(md5)
            print(sha1)
            print(sha256)

            hashlist=[md5,sha1,sha256]
            with open (outputFile,"a", newline= '') as file:
                csvwriter=csv.writer(file)
                csvwriter.writerow(hashlist)
        #else:
            #put api for malware bazzaar or anomali threat stream here
        else:
            md5="Not Found"
            sha1="Not Found"
            sha256="Not Found"
            print(md5)
            print(sha1)
            print(sha256)
            hashlist=[md5,sha1,sha256]
            with open(outputFile,"a",newline= '') as file:
                csvwriter=csv.writer(file)
                csvwriter.writerow(hashlist)
    

