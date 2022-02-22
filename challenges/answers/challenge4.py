# Challenge 4

#   Description:
#   
#   In this challenge, you should write a function to convert some number of seconds
#   into hours, minutes and seconds. 
#
#   The seconds to be converted will be passed as a
#   command line argument, and erroneous cases should be handled correctly.
#   
#   Note briefly: it is not a problem if your function prints 0 for either minutes or hours
#   if the they divide into them exactly. You should ignore any remainder seconds that are passed.
#
#   It also doesn't matter whether they are printed
#   on the same or different lines.
#
#   Example test cases:
#
#   py challenge1.py 0 -> 0h, 0m, 0s
#   py challenge1.py 1 -> 0h, 0m, 1s
#   py challenge1.py 180 -> 0h, 3m, 0s
#   py challenge1.py 1810 -> 0h, 30m, 10s
#   py challenge1.py 19800 -> 5h, 30m, 0s
#   py challenge1.py -1 -> Error (as we can't go back in time)
#   py challenge1.py "hell9" -> Error

CHALLENGE = 4

def main():
    pass

if __name__ == "__main__":
    print("Challenge %d" % CHALLENGE)
    print()
    main()