from game import Game
import sys

def main(args: list):
    if len(args) != 3:
        print("You must provide a width and height for the program")
        return

    try: 
        size = int(args[1])
    except:
        print("Width and height must be integers")
        return

    # Play the game
    g = Game(size)
    g.play()

if __name__ == "__main__":
    main(sys.argv)