#the goal of this is code is to show the ability to take input form a csv file and use it within the acutal code
import csv

# I might use a list to add stuff to it and then write it to a file later
#array=[[row," ","meow"]]






# assigning a file to a variable
file = "/Users/deadlenny/Library/CloudStorage/OneDrive-Personal/Documents/test.csv" # ideally replace this to take input from the commandline for the filename

# reading a file
with open(file) as csvfile:
    csvreader=csv.reader(csvfile) 
    for row in csvreader:
        print(row)
        with open("/Users/deadlenny/Library/CloudStorage/OneDrive-Personal/Documents/output.csv","a") as file:
            csvwriter=csv.writer(file)
            array=[" meow"] # replace meow with a veriable that will store the output of whether the chrome extensions is True or False
            csvwriter.writerow(row + array)
            #csvwriter.writerow("meow")
            




#print(array)