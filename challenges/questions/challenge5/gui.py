import tkinter as tk

class GUI:
    def __init__(self, grid_size: int, window_size: int = 720, title = "Snake by Cosmin"):
        self.window = tk.Tk()
        self.window.title(title)

        self.grid_size = grid_size
        self.window_size = window_size

        self.updates = 0

        self.cancelled = False

        self.canvas = tk.Canvas()
        self.canvas = tk.Canvas(self.window, width=window_size, height=window_size, bg='black')
        self.canvas.pack()
        self.canvas.focus_set()

        self.loopFunc = None

        # Set the window size
        self.square_size = int(window_size / grid_size)

    def loop(self, updateFunc, waitTime):
        self.updates += 1

        return_time = updateFunc()

        if return_time is not None: waitTime = return_time

        if not self.cancelled:
            self.loopFunc = self.canvas.after(waitTime, self.loop, updateFunc, waitTime)

    def cancel_loop(self):
        if self.loopFunc is None:
            return

        self.cancelled = True

        self.canvas.after_cancel(self.loopFunc)

    def bind_keypress(self, function):
        self.canvas.bind("<Key>", function)

    def unbind_keypress(self):
        self.canvas.unbind("<Key>")

    def show_debug_text(self, val):
        for debug_text in self.canvas.find_withtag("debug"):
            if val: self.canvas.itemconfig(debug_text, state='normal')
            else: self.canvas.itemconfig(debug_text, state='hidden')

    # Draw methods

    def draw_square(self, x: int, y: int, color='white'):
        rect = self.canvas.create_rectangle(x * self.square_size, y * self.square_size, # x1, y1
            (x + 1) * self.square_size , (y + 1) * self.square_size, # x2, y2
                fill=color, tags="SQUARE") # Colour of the square

        self.canvas.tag_lower(rect)
        
    def add_text(self, x, y, text = "NO TEXT", *names, debug = False, text_color='white'):
        tags = list(names)
        if debug: tags.append("debug")
        
        text = self.canvas.create_text(x, y, fill=text_color, text=text, tags=tags, font=("Arial", 16), anchor= tk.NW)

        if debug:
            self.canvas.itemconfig(text, state='hidden')

        self.canvas.tag_raise(text)

    def update_text(self, name, newtext):
        self.canvas.itemconfig(name, text=newtext)

    def move_text(self, name, x, y):
        self.canvas.moveto(name, x, y)

    def delete_text(self, *names):
        for name in names:
            self.canvas.delete(name)

    def delete_squares(self):
        self.canvas.delete("SQUARE")