from gui import GUI

class Game:
    def __init__(self, size: int):
        self.grid_size = size

        self.gui = GUI(size)

    def play(self):
        # TO ADD: Game looping function here

        # Do not remove the next line
        self.gui.window.mainloop()