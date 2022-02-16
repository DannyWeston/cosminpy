# Challenge 1
#
#   Description:
#
#   In this challenge you should create a program which prints out the even 
#   numbers up-to (and including) a single integer passed as an argument.
#
#   It does not matter how these numbers are printed (new lines or the same line)
#   Erroneous cases should be handled (consider them to be any negative integer)
#
#   Example test cases:
#
#   py challenge1.py 7 -> 0 2 4 6
#   py challenge1.py 12 -> 0 2 4 6 8 10 12
#   py challenge1.py -1 -> Error

import sys

CHALLENGE = 1

def main():
    # Check correct num of arguments passed
    if len(sys.argv) != 2:
        print("Error: only 2 arguments should be passed!")
    
    # get a from sys args
    a = sys.argv[1]

    # Convert a from string to int
    try: 
        a = int(a)
    except: 
        print("Error: integer input needs to be an input!")
        return

    # Check if a < 0
    if a < 0:
        print("Error: argument cannot be negative!")
        return

    # Run a for loop from 0 to a, increase counter by 2 each iteration
    counter = 0
    while counter <= a: 
        print(counter)
        counter += 2

if __name__ == "__main__":
    print("Challenge %d" % CHALLENGE)
    print()
    main()