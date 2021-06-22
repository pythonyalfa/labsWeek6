# Task 04
# Consider the following list of student grades. Write a script that will open the ﬁle and#
# calculate the average for each student and the grade that the student would receive
# based on the grade scale for this course found in the syllabus. It should save the output
# to a ﬁle named out604.txt

# importing csv module
import csv

# csv file name
filename = "lab0604.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

#  printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    # parsing each column of a row
    for col in row:
        print("%10s"%col),
    print('\n')