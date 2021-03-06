# Challenge 2
#
#   Description:
#
#   In this challenge, you are to print out the reverse of a string without
#   using a built in method - that is, you should use some form of loop accordingly.
#   
#   The string will be inputted via usage of a command line parameter.
#
#   Example test cases:
#
#   py challenge2.py "hello" -> olleh
#   py challenge2.py "my name is daniel" -> leinad si eman ym
#   py challenge2.py "a" -> a
import sys

CHALLENGE = 2

def main():
    if len(sys.argv) != 2:
        print("You must input only 1 string argument")
        return
    
    a = sys.argv[1]
    size = len(a)

    reverse = ""
    for i in range(0, size):
        reverse += a[size - i - 1]

    print(reverse)


if __name__ == "__main__":
    print("Challenge %d" % CHALLENGE)
    print()
    main()