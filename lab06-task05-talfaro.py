#!/usr/bin/python3
# Write a Python script that will take in a name and return the respective address based
# on a csv file of names and addresses.csv. If the name is not found in the ﬁle, prompt the
# user to enter an address for that name and add it to the ﬁle.

import csv

def main():
    name = "Josephine"
    with open("addresses.csv", "r") as addressFile:
        f = csv.DictReader(addressFile)
        for row in addressFile:
            if row[0] == name:
                print("Address: ", (row[1]))
            if row[0] != name:
                addressFile = open("addresses.csv", "a+")
                ask = input("Name not in address book, would you like to add? yes / no ")
            if ask == "no":
                for row in addressFile:
                    print(row)
            if ask == "yes":
                address = input("Address: ")
                addressFile.write(f"\n{name}:{address}\n")


    addressFile.close()

main()

#for row in addressReader:
 #   print(row)
