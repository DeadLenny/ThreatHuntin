
import urllib.request, urllib.error
import csv

#website="https://chrome.google.com/webstore/detail/"

#guid="jghecgabfgfdldnmbfkhmffcabddioke"#replace this with a variable for the read


#request= website+guid

#try:
    #status_code= urllib.request.urlopen(request).getcode()
    #print(True)
#except urllib.error.HTTPError as err:
    #print(False)

Bool=False


inputFile ="/Users/deadlenny/Library/CloudStorage/OneDrive-Personal/Documents/test.csv"
outputfile="/Users/deadlenny/Library/CloudStorage/OneDrive-Personal/Documents/output.csv"

with open(inputFile) as csvfile:
    csvreader=csv.reader(csvfile)
    for row in csvreader:
        #print(row)
        website="https://chrome.google.com/webstore/detail/"
        #create a variable that takes the string in the row variable and assign it to guid
        guid=""
        for char in row:
            if char.isalpha()==True:
                guid+=char
        #guid=str(row) 
        print(guid)
        request= website+guid
        try:
            status_code= urllib.request.urlopen(request).getcode()
            Bool=True
            #print(True)
        except urllib.error.HTTPError as err:
            Bool=False
            #print(False)
        with open(outputfile,"a") as file:
            csvwriter=csv.writer(file)
            array=[" "+str(Bool)]
            csvwriter.writerow(row + array)
















#status_code= urllib.request.urlopen(request).getcode()
            #website_status= status_code==200 
#if status_code ==200:
    #print(True)
#else:
    #print(False)

#print(website_status)










