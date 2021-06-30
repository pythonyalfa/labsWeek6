# Task 04
# Consider the following list of student grades. Write a script that will open the file and
# calculate the average for each student and the grade that the student would receive
# based on the grade scale for this course found in the syllabus. It should save the output
# to a ﬁle named out604.txt

# importing csv module


# This method didn't work, scratch it : )
# def main():
#   asList = open('lab0604.csv', 'r')
# for i in asList.readline():
#      for i in asList.readlines():
#         print(sum(i))
#        print(i)
#       print(sum([int(i)
#                  for i in asList.split() if str(i).isdigit()]))

# main()

def average(x, added):
    average = added / 8                          # According to the Syllabus
    f = open("lab0604.csv", "r+")
    f.readline()

    for line in f:
        x = line.split(",")
        g = open("0604.txt", "a+")



    if average >= 97:                             #Letter > 97% A+
        #print(x[0], average, "A+")
        average = added / 8                          # According to the Syllabus
        f = open("lab0604.csv", "r+")
        f.readline()

        for line in f:
            x = line.split(",")
            g = open("0604.txt", "a+")
            g.writelines(f"\n{x[0]} {average}\n")

    elif 94 <= average <= 96.99:                      #94% to 96% A
        #print(x[0], average, "A")

        f = open("lab0604.csv", "r+")
        f.readline()

        for line in f:
            x = line.split(",")
            g = open("0604.txt", "a+")
            g.writelines(f"\n{x} {average} A \n")
    elif 90 <= average <= 93.99:                      #90% to 93% A-
        #print(x[0], average, "A-")
    f = open("lab0604.csv", "r+")
    f.readline()

    for line in f:
        x = line.split(",")
        g = open("0604.txt", "a+")
        g.writelines(f"\n{x} {average} A \n")
#        g.writelines(f"\n{x} {average} A- \n")
    elif 87 <= average <= 89.99:                      #87% to 89% B+
        #print(x[0], average, "B+")
 #       g.writelines(f"\n{x} {average} B+ \n")
    f = open("lab0604.csv", "r+")
    f.readline()

    for line in f:
        x = line.split(",")
        g = open("0604.txt", "a+")
        g.writelines(f"\n{x} {average} A \n")
    elif 84 <= average <= 86.99:                      #84% to 86% B
        #print(x[0], average, "B")
#        g.writelines(f"\n{x} {average} B \n")
    f = open("lab0604.csv", "r+")
    f.readline()

    for line in f:
        x = line.split(",")
        g = open("0604.txt", "a+")
        g.writelines(f"\n{x} {average} A \n")
    elif 80 <= average <= 83.99:                      #80% to 83% B-
        #print(x[0], average, "B-")
#        g.writelines(f"\n{x} {average} B- \n")
    f = open("lab0604.csv", "r+")
    f.readline()

    for line in f:
        x = line.split(",")
        g = open("0604.txt", "a+")
        g.writelines(f"\n{x} {average} A \n")
    elif 76 <= average <= 79.99:                      #76% to 79% C+
        #print(x[0], average, "C+")
#        g.writelines(f"\n{x} {average} C+\n")
    f = open("lab0604.csv", "r+")
    f.readline()

    for line in f:
        x = line.split(",")
        g = open("0604.txt", "a+")
        g.writelines(f"\n{x} {average} A \n")
    elif 70 <= average <= 75.99:                      #70% to 75% C
        #print(x[0], average, "C")
#        g.writelines(f"\n{x} {average} C\n")
    f = open("lab0604.csv", "r+")
    f.readline()

    for line in f:
        x = line.split(",")
        g = open("0604.txt", "a+")
        g.writelines(f"\n{x} {average} A \n")

    elif 60 < average <= 69.99:                       #60% to 69% D
        #print(x[0], average, "D")
#        g.writelines(f"\n{x} {average} D \n")
    f = open("lab0604.csv", "r+")
    f.readline()

    for line in f:
        x = line.split(",")
        g = open("0604.txt", "a+")
        g.writelines(f"\n{x} {average} A \n")
    elif average <= 60.99:                               #< 60% E
        #print(x[0], average, "E")
#        g.writelines(f"\n{x} {average} E\n")
    f = open("lab0604.csv", "r+")
    f.readline()

    for line in f:
        x = line.split(",")
        g = open("0604.txt", "a+")
        g.writelines(f"\n{x} {average} A \n")

    else:
        print("Goodybye! ")
        f.close()
        #added = sum(int(number) for number in x[1:])  # sum up the numbers in each line
        #average(x, added)

        #g.writelines(f"\n{x[0]} {average}\n")
        #g.close()

def main():
    f = open("lab0604.csv", "r+")
    f.readline()

    for line in f:

        x = line.split(",")
        g = open("0604.txt", "a+")

        added = round(sum(int(number) for number in x[1:]))  # sum up the numbers in each line
        g.writelines(f"\n{x[0]} {added}\n")


        g.close()

        #g.writelines(average(x,added))




        average(x, added)
main()
