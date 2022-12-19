import random
import os
import logging
import msvcrt

class Snake:
    snake_score = 0
    board_width = 0
    board_height = 0
    apple_pos = []
    snake_parts = []

    # Constructor
    def __init__(self, board_width, board_height):
        self.board_width = board_width
        self.board_height = board_height
        # Update the snake_parts
        self.snake_parts = [[self.board_width//2, self.board_height//2]]
        #self.snake_parts = self.board_width
    # Update the snake_parts with new coords
    # Check if game ended
    def check_game_ended(self):
        for coord in self.snake_parts:
            if self.snake_parts.count(coord) > 1:
                print(f'\nYou lost! Your score was {self.snake_score}')
                return True
        return False
    # Make snake taller and add score
    def make_snake_taller(self):
        self.snake_score += 1
        logging.info(f'Snake parts are: {self.snake_parts}')
        # At first you add it to a random axes and every other time it adds to the axes
        if self.snake_score > 1:
            coord_of_tail = self.snake_parts[-1]
            coord_of_body = self.snake_parts[-2]
            if coord_of_tail[1] == coord_of_body[1]:
                if coord_of_tail[0] > coord_of_body[0]:
                    self.snake_parts.append([coord_of_tail[0] + 1, coord_of_tail[1]])
                else:
                    self.snake_parts.append([coord_of_tail[0] - 1, coord_of_tail[1]])
            elif coord_of_tail[0] == coord_of_body[0]:
                if coord_of_tail[1] > coord_of_body[1]:
                    self.snake_parts.append([coord_of_tail[0], coord_of_tail[1] + 1])
                else:
                    self.snake_parts.append([coord_of_tail[0], coord_of_tail[1] - 1])
        else:
            coord_of_tail = self.snake_parts[-1]
            self.snake_parts.append([coord_of_tail[0] + 1, coord_of_tail[1]])
    # Create apple
    def create_apple(self):
        range_width = list(range(self.board_width))
        range_height = list(range(self.board_height))
        logging.info(f'Range for width is: {range_width}, range for height is: {range_height}')
        for x, y in self.snake_parts:
            logging.info(f'{x}, {y}')
            if x in range_width:
                range_width.remove(x)
            if y in range_height:
                range_height.remove(y)
        rand_width = random.choice(range_width)
        rand_height = random.choice(range_height)

        self.apple_pos = [rand_width, rand_height]
        logging.info(f'Position of the apple is: {self.apple_pos}')
        logging.info(f'Position of the snake is: {self.snake_parts}')

    # Make snake move
    def move(self):
        key = msvcrt.getwch()
        #key = key.split('')
        logging.info(f'Pressed key is: {key}, type for key is: {type(key)}')
        # Move tail to the head easy fix
        if key == 'w':
            head = self.snake_parts[0]
            self.snake_parts.insert(0, [head[0], head[1]-1])
            self.snake_parts.remove(self.snake_parts[-1])
        elif key == 's':
            head = self.snake_parts[0]
            self.snake_parts.insert(0, [head[0], head[1]+1])
            self.snake_parts.remove(self.snake_parts[-1])
        elif key == 'a':
            head = self.snake_parts[0]
            self.snake_parts.insert(0, [head[0]-1, head[1]])
            self.snake_parts.remove(self.snake_parts[-1])
        elif key == 'd':
            head = self.snake_parts[0]
            self.snake_parts.insert(0, [head[0]+1, head[1]])
            self.snake_parts.remove(self.snake_parts[-1])
        else:
            logging.info("No key is pressed")
    # Print the board
    def print_board(self):
        # nt being the os name for windows
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print('#'*(self.board_width+2), end='')
        print(f'\t\t Score: {self.snake_score}')
        for y in range(self.board_height):
            print('#', end='')
            for x in range(self.board_width):
                if [x, y] in self.snake_parts:
                    print('X', end='')
                elif [x, y] == self.apple_pos:
                    print('@', end='')
                else:
                    print(' ', end='')
            print('#')
        print('#'*(self.board_width+2))
    # Check if snake eat the apple
    def check_eat_apple(self):
        for coord in self.snake_parts:
            if coord == self.apple_pos:
                self.make_snake_taller()
                return True
        return False

def main():
    logging.basicConfig(level=logging.INFO, filename='snake.log', filemode='w')
    # Create the class instance
    snake = Snake(27, 13)
    # Create apple for the beginning of the game
    snake.create_apple()
    # Game loop
    while (True):
        # Check if game ended
        if snake.check_game_ended() == True:
            break
        # Print the board
        snake.print_board()
        # Make snake move
        # This input logic is bad because you need to wait for an input
        # TODO Fix this
        snake.move()
        # Check if apple eaten
        if snake.check_eat_apple() == True:
            # Create apple
            # For some reason sometimes the apple wont some up
            snake.create_apple()
if __name__ == '__main__':
    main()