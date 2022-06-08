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


import requests
import csv
import json
import os
from dotenv import load_dotenv
load_dotenv()


#File path for input and output of the results, if output file doesn't exist it will be created

inputFile= os.getenv("HOME")+"TestHashes2.csv "
outputFile=os.getenv("HOME")+"TestHashesOutput.csv "

#Virustotal API for sending a request
headers = {
    "Accept": "application/json",
    #virustotal api key is stored in environment variable
    "x-apikey": os.getenv("api_key_vti")
}
#Malware Bazaar Api for sending stuff
data= {
    "query":"get_info",
    "hash":""
}

#header for the output csv file, top row
csvheader=['MD5','SHA1','SHA256']

#Disables all the annoying insecure request warning
requests.packages.urllib3.disable_warnings()

#Counter variable to show hashes completed from list
Count=0



#input file reaads input
with open(inputFile)as csvfile:
    csvreader=csv.reader(csvfile)
    #writing the header for the output file
    with open(outputFile, "w",newline= '')as file:
        csvwriter=csv.writer(file)
        csvwriter.writerow(csvheader)

    #loop for each row in the inputfile    
    for row in csvreader:
        HASH=""
        #parsing out the letters and numbers from the file reader
        for char in row:
            HASH+=char

        #Updating data dictionary for malware bazaar api
        h1={"hash":HASH}
        data.update(h1)



        #gets request from the virustotal api
        url = f"https://www.virustotal.com/api/v3/files/{HASH}"
        response = requests.request("GET", url, headers=headers, verify = False)
        print(HASH)

        #malware bazaar request response from api
        Malurl="https://mb-api.abuse.ch/api/1/"
        Malresponse= requests.post(Malurl, data=data, verify = False)

        #checking for if virustotal has anything for the hash
        if response.status_code==200:
            #raw virustotal reponse 
            x=json.loads(response.text)

            #using json to find the hash values
            md5=(x["data"]["attributes"]["md5"])
            sha1=(x["data"]["attributes"]["sha1"])
            sha256=(x["data"]["attributes"]["sha256"])

            Count+=1

            #Printing content for user visuals
            print("MD5: "+md5)
            print("SHA1: "+sha1)
            print("SHA256 :"+sha256)
            print("Current number of hashes completed: "+ str(Count))
            print("----------------------")

            #writing out the hashes to the outputfile
            hashlist=[md5,sha1,sha256]
            with open (outputFile,"a", newline= '') as file:
                csvwriter=csv.writer(file)
                csvwriter.writerow(hashlist)

        #Moving to Malware Bazaar Api if virustotal has nothing        
        elif "query_status" and "ok" in Malresponse.text:
            
            #raw Malware Bazaar reponse 
            x=json.loads(Malresponse.text)

            #Parsing Json response for hashes
            md5= (x["data"][0]["md5_hash"])
            sha1= (x["data"][0]["sha1_hash"])
            sha256= (x["data"][0]["sha256_hash"])

            Count+=1

            #Printing content for user visuals
            print("MD5: "+md5)
            print("SHA1: "+sha1)
            print("SHA256 :"+sha256)
            print("Current number of hashes completed: "+ str(Count))
            print("----------------------")

            hashlist=[md5,sha1,sha256]
            with open (outputFile,"a", newline= '') as file:
                csvwriter=csv.writer(file)
                csvwriter.writerow(hashlist)
        #elif:
            #put anomali threat stream and or other malware hashlookup softwares here.

        #default response if virustotal has nothing
        else:
            md5="Not Found"
            sha1="Not Found"
            sha256="Not Found"
            Count+=1

            #Printing content for user visuals
            print("MD5: "+md5)
            print("SHA1: "+sha1)
            print("SHA256 :"+sha256)
            print("Current number of hashes completed: "+ str(Count))
            print("----------------------")

            hashlist=[md5,sha1,sha256]
            with open(outputFile,"a",newline= '') as file:
                csvwriter=csv.writer(file)
                csvwriter.writerow(hashlist)
