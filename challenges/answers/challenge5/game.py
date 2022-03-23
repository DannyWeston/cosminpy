import math
from random import randint

from gui import GUI

Board = list[list[int]]
Snake = list[tuple[int, int]]

Tile = {
    "Empty" : 1,
    "Snack" : 2,
    "Snake" : 3
}

class Game:
    STARTING_DIFFICULTY = 400

    def __init__(self, size: int):
        self.size = size

        self.gui = GUI(size)

        self.score = 0

        self.snake_vel = (1, 0)

        self.board = self.empty_board()

        self.snake = self.new_snake()

        self.debug = False

        # Add a random snack to the board
        self.add_random_snack()

        # Register key listen events
        self.gui.bind_keypress(self.handle_key_press)
        
        # Scoreboard text
        self.gui.add_text(25, 25, "Score: " + str(self.score), "score_text")

        # Debug text
        self.gui.add_text(25, self.gui.window_size - 50, "Updates: " + str(self.gui.updates), "update_text", debug=True)
        self.gui.add_text(25, self.gui.window_size - 100, "Velocity: " + str(self.snake_vel), "velocity_text", debug=True)

    def play(self):
        # Don't change the next things
        self.gui.loop(self.update, Game.STARTING_DIFFICULTY)
        self.gui.window.mainloop()

    def empty_board(self):
        return [[Tile["Empty"] for _ in range(self.size)] for _ in range(self.size)]

    def add_random_snack(self):
        while True:
            x = randint(0, self.size - 1)
            y = randint(0, self.size - 1)

            if (x, y) not in self.snake:
                self.board[x][y] = Tile["Snack"]
                return

    def new_snake(self):
        snake_len = int(math.sqrt(self.size))

        return [(x, 0) for x in range(0, snake_len)]

    def try_change_velocity(self, vel):
        if self.calc_next_position(self.snake[-1], vel) != self.snake[-2]:
            self.snake_vel = vel

    def handle_key_press(self, e):
        if e.keysym == 'Up' or e.keysym == 'w': # Up arrow key is pressed
            self.try_change_velocity((0, -1))

        elif e.keysym == 'Down' or e.keysym == 's': # Down arrow key is pressed
            self.try_change_velocity((0, 1))

        elif e.keysym == 'Left' or e.keysym == 'a': # Left arrow key is pressed
            self.try_change_velocity((-1, 0))

        elif e.keysym == 'Right' or e.keysym == 'd': # Right arrow key is pressed
            self.try_change_velocity((1, 0))
        
        elif e.keysym == 'Escape': # Right arrow key is pressed
            self.gui.window.quit()
            quit()

        elif e.keysym == 'F1': # F1 key is pressed\
            self.debug = not self.debug
            self.gui.show_debug_text(self.debug)

    def calc_difficulty(self):
        return Game.STARTING_DIFFICULTY - int(100 * math.log10(self.score + 1))

    def calc_next_position(self, pos, vel):
        return ((pos[0] + vel[0]) % self.size, (pos[1] + vel[1]) % self.size)

    def update(self):
        # Update snake pos
        (head_x, head_y) = self.calc_next_position(self.snake[-1], self.snake_vel)

        # Check if theres a snack there
        if self.board[head_x][head_y] == Tile["Snack"]:
            # Remove the snack and extend the snake
            self.board[head_x][head_y] = Tile["Empty"]
            self.snake.append((head_x, head_y))

            # Increase the score by 1
            self.score += 1

            # Add a random snack
            self.add_random_snack()

        else:
            # Move the snake along by 1
            self.snake = self.snake[1:] + [(head_x, head_y)]

        # Check for game over
        if len(self.snake) != len(set(self.snake)):
            self.game_over()

            return None

        # Draw everything after being updated
        self.draw()

        # Return the wait time depending upon the score
        return self.calc_difficulty()
 
    def draw(self):
        # Update text 
        self.gui.update_text("update_text", "Updates: " + str(self.gui.updates))
        self.gui.update_text("velocity_text", "Velocity: " + str(self.snake_vel))
        self.gui.update_text("score_text", "Score: " + str(self.score))

        # Clear the canvas of squares
        self.gui.delete_squares()

        # Draw the snake head
        (head_x, head_y) = self.snake[-1]
        self.gui.draw_square(head_x, head_y, 'green')

        # Draw the snake body
        for (x, y) in self.snake[:-1]:
            self.gui.draw_square(x, y, 'spring green')
        
        # Draw the snacks
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] == Tile['Snack']:
                    self.gui.draw_square(x, y, 'red')

    def game_over(self):
        # Cancel the game loop
        self.gui.cancel_loop()
        self.gui.unbind_keypress()

        # Delete all squares
        self.gui.delete_squares()

        # Hide all debug text
        self.debug = False
        self.gui.show_debug_text(False)

        # Show game over label
        self.gui.add_text(25, 25, "Game over!", "game_over_text")

        # Move score text
        self.gui.move_text("score_text", 25, 75)