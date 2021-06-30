#!/usr/bin/python3

#This is just to create the file
addresses = open("./addresses.csv", "a+")
addresses.write(f"Bob:321 Test St\n")
addresses.close()


name = "Alice"
address = "123 Test St"

addresses = open("./addresses.csv", "r+")
for i in addresses.readlines():
    if "Alice:123 Test St" in i:
        print(i)
    else:
        addresses.close()
        addresses = open("./addresses.csv", "a+")
        addresses.write(f"{name}:{address}\n")
        addresses.close()
        break

name,hw1,h2,h3,hw4,lb1,lb2,lb3,lb4
Andrew,69,52,32,83,22,33,77,34
Brandon,87,80,79,85,99,92,77,80
Chelsey,98,97,91,92,93,99,91,94
Deborah,51,61,28,58,34,53,74,39
Erik,80,88,97,88,102,106,86,94
Arielle,73,73,88,79,73,80,90,82
Shaun,61,76,77,69,71,80,74,67
Ninette,88,67,28,42,51,66,57,43
Nguyen,5,23,93,60,31,25,65,23