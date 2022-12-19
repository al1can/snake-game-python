import random
import os
import logging
import msvcrt
import sys
import getopt
import time

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
        self.snake_parts = [[self.board_width//2+1, self.board_height//2],
                            [self.board_width//2, self.board_height//2],
                            [self.board_width//2-1, self.board_height//2]]
    # Check if game ended
    def check_game_ended(self):
        for coord in self.snake_parts:
            if self.snake_parts.count(coord) > 1:
                print(f'\nYou lost! Your score was {self.snake_score}!')
                return True
        return False
    # Make snake taller and add score
    def make_snake_taller(self):
        self.snake_score += 1
        logging.info(f'Snake parts are: {self.snake_parts}')
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
    # Create apple
    def create_apple(self):
        range_width = list(range(self.board_width))
        range_height = list(range(self.board_height))
        logging.info(f'Range for width is: {range_width}, range for height is: {range_height}')
        for x, y in self.snake_parts:
            logging.info(f'Snake part position x: {x}, y: {y}')
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
    def move(self, prev_key, difficulty):
        key = None
        if msvcrt.kbhit():
            key = msvcrt.getwch()
        # If there is no active pressed key snake moves in the previous keys direction
        if key is None:
            key = prev_key
        if difficulty == 1:
            time.sleep(0.2)
        elif difficulty == 2:
            time.sleep(0.1)
        elif difficulty == 3:
            time.sleep(0.05)
        #key = key.split('')
        logging.info(f'Pressed key is: {key}, type for key is: {type(key)}')
        # Move tail to the head easy fix
        if key == 'w':
            head = self.snake_parts[0]
            self.snake_parts.insert(0, [head[0]%self.board_width, (head[1]-1)%self.board_height])
            self.snake_parts.remove(self.snake_parts[-1])
        elif key == 's':
            head = self.snake_parts[0]
            self.snake_parts.insert(0, [head[0]%self.board_width, (head[1]+1)%self.board_height])
            self.snake_parts.remove(self.snake_parts[-1])
        elif key == 'a':
            head = self.snake_parts[0]
            self.snake_parts.insert(0, [(head[0]-1)%self.board_width, head[1]%self.board_height])
            self.snake_parts.remove(self.snake_parts[-1])
        elif key == 'd':
            head = self.snake_parts[0]
            self.snake_parts.insert(0, [(head[0]+1)%self.board_width, head[1]%self.board_height])
            self.snake_parts.remove(self.snake_parts[-1])
        return key
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
                    print('0', end='')
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
    # Default width and height
    width = 27
    height = 13
    difficulties = ['easy', 'medium', 'hard']
    # Default difficulty is medium
    difficulty = 2
    # Accepting arguments from cli for setting height and width and displaying help
    args_list = sys.argv[1:]
    short_opts = "x:y:d:h"
    long_opts = ["width=", "height=", "difficulty=", "help"]
    try:
        options, arguments = getopt.getopt(args_list, shortopts=short_opts, longopts=long_opts)
        for opt, arg in options:
            logging.info(f'Options are: {opt}, arguments are: {arg}')
            if opt in ('-x', '--width'):
                width = int(arg)
            elif opt in ('-y', '--height'):
                height = int(arg)
            elif opt in ('-d', '--difficulty'):
                if int(arg) in (1, 2, 3):
                    difficulty = int(arg)
                else:
                    print("Desired difficulty is not available!")
                    print("You can use the following options")
                    print('\t1. Easy\n\t2. Medium \n\t3. Hard')
                    sys.exit()
            elif opt in ('-h', '--help'):
                print('           /^\/^\\')
                print('         _|__|  O|')
                print('\/     /~     \_/ \\')
                print('\____|__________/  \\')
                print('        \_______      \\')
                print('                `\     \                    \\')
                print('                /     /                       \\')
                print('                 /      /                    \\ \ ')
                print('                /     /                       \\ \ ')
                print('              /      /                         \ \\ ')
                print('             /     /                            \  \\ ')
                print('           /     /             _----_            \   \\')
                print('          /     /           _-~      ~-_         |   |')
                print('         (      (        _-~    _--_    ~-_     _/   |')
                print('          \      ~-____-~    _-~    ~-_    ~-_-~    /')
                print('            ~-_           _-~          ~-_       _-~')
                print('               ~--______-~                ~-___-~')
                print('This is a terminal snake game written in Python')
                print('This basic game is created by Ali Can Gunduz')
                print('You can set the width with the options -x or --width')
                print('and height with the options -y or --height')
                print(f'Default values are {width} for width and {height} for height')
                print('You can change the difficulty too')
                print('Available diffuculties \n\t1. Easy\n\t2. Medium \n\t3. Hard')
                sys.exit()
    except getopt.error as err:
        print(str(err))
    logging.basicConfig(level=logging.INFO, filename='snake.log', filemode='w')
    # Create the class instance
    snake = Snake(width, height)
    # Create apple for the beginning of the game
    snake.create_apple()
    # When the game start the default direction is right
    prev_key = 'd'

    # Game loop
    while (True):
        # Check if game ended
        if snake.check_game_ended() == True:
            break
        # Print the board
        snake.print_board()
        # Make snake move
        prev_key = snake.move(prev_key, difficulty)
        # Check if apple eaten
        if snake.check_eat_apple() == True:
            # Create apple
            snake.create_apple()

if __name__ == '__main__':
    main()