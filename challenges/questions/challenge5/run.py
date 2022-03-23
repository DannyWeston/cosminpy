from game import Game
import sys

def main(args: list):
    if len(args) != 2:
        print("You must provide a size for the board!")
        return

    try: 
        size = int(args[1])
    except:
        print("Size must be an integer")
        return

    # Play the game
    g = Game(size)
    g.play()

if __name__ == "__main__":
    main(sys.argv)