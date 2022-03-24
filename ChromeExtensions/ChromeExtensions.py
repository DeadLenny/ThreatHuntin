
import urllib.request, urllib.error
import csv


Bool=False


inputFile =" " #Input file name here to pull the list of chrome extensions from, could also change this to take arguments when executing the script instead
outputfile="output.csv" # choose the file you would like to ouput the results to, if there isn't a file with this name then a file should be created in the current direcotry


with open(inputFile) as csvfile:
    csvreader=csv.reader(csvfile)
    for row in csvreader:
        website="https://chrome.google.com/webstore/detail/"
        guid=""
        for char in row:
            if char.isalpha()==True:
                guid+=char
        print(guid)
        request= website+guid
        try:
            status_code= urllib.request.urlopen(request).getcode()
            Bool=True
        except urllib.error.HTTPError as err:
            Bool=False
        with open(outputfile,"a") as file:
            csvwriter=csv.writer(file)
            array=[" "+str(Bool)]
            csvwriter.writerow(row + array)

