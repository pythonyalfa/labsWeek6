# Task - 03 Write a Python script that will simulate a dice roll.It should continually prompt for a
# number of sides and then return a random number thatmight be rolled with a die of that
# number of sides. Assume a standard die that starts at 1 and goes to the given number
# of sides.
# Input string                  Expected output of script
# Enter number of sides: 4      Roll: 2
# Enter number of sides: 6      Roll: 4
# Enter number of sides: 20     Roll: 11






import random
import time


def main():
    x = eval(input("How many sids on the dice (Enter 0 to quit): "))            # Begin by asking user for a number to represent how many sides a dice has

    while x != 0:                                                               # While loop to continously ask user for input until they enter zero
        print("Rolling die...")
        time.sleep(.75)
        print ("Die landed on ", random.randint(1,x))                           # Call to the random module to print out a pseudo random number
        x = eval(input("How many sides on the dice (Enter 0 to quit): "))       # input loops until user enters zero

#        if x == 0:
            #print("Goodbye!")
        #dice = input("How many sides on the dice ? <enter> to quit: ")
        #print ("Free roll: ", random.randint(1,x))
    print("Goodybye!")                                                          # Exit message for user
main()                                                                          #Call the main function