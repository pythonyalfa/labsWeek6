# Write a Python script that will prompt for the scores of the 6 homework and 7 lab
# assignments in this course, and then calculate the amount of extra credit you would
# need in order to get a 90% or higher in the class.You are allowed to ask for the scores to
# be entered in any format and in as many prompts as you like.
# Input string                          Expected output of script
# Enter your hw scores:                 You need at least 85 points of extra credit
# 30, 35, 30, 35, 40, 40                to get a 90% in this class.
# Enter your lab scores:
# Enter your lab scores:
# 80, 80, 85, 80, 90, 90, 100
#CtrlD will copy paste in one move
import math


def scores(hwscore, labscore):                                          # This function calculates the students grades
    hw = (sum(hwscore))
    lab = (sum(labscore))
    sumofBoth = hw+lab
    percentofTotal = (sumofBoth/1000) * 1000
    points = 900 - percentofTotal
    return points



# We need a percentage of 1000 so many points is what percent of 1000
def main():
    points = 0
    hwscores = 30, 35, 30, 35, 40, 40                                   # Homework scores
    labscores = 80, 80, 85, 80, 90, 90, 100                             # Labs score

    #hwscores = eval(input("Enter your hw scores: "))

    #labscores = eval(input("Enter your lab scores: "))
    print("You need at least,", scores(hwscores, labscores)," points to get a 90% in this class.")      # Call to function that displays points needed to receive a 90% in the class




main()