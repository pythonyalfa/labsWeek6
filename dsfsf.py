#!/usr/bin/python3
# Write a Python script that will take in a name and return the respective address based
# on a csv file of names and addresses.csv. If the name is not found in the ﬁle, prompt the
# user to enter an address for that name and add it to the ﬁle.

import csv

def addtoAddressBook(name):
    address = input("Address: ")
    # field names


    # name of csv file


    # writing to csv file
    with open("github/simpleCsvParser/addresses.csv", 'a') as csvfile:
        #creating a csv writer object
        writeToFile = csv.writer(csvfile)
        #writing the data rows
        writeToFile.writerow(name)
        writeToFile.writerow(address)

        #writeToFile.writerow({"Name" : (name), "Address": (address)})
    return name, address







name = input("Enter name: ")

with open("github/simpleCsvParser/addresses.csv", newline='') as addressFile:
    addressReader = csv.DictReader(addressFile, delimiter=",")
    for allRows in addressReader:
        #print(allRows)
        #addressFile.close()


        with open("github/simpleCsvParser/addresses.csv", newline='') as addressFile2:
            addressReader2 = csv.DictReader(addressFile2, delimiter=",")
            for row in addressReader2:


            if row['Name'] == name:
                print("Address: ",(row['Address']))

                addressFile2.close()


