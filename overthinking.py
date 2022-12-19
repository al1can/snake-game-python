# im gonna put the stupidest things
# that i wrote here to look back and 
# say well i do stupid things when i overthink
if self.snake_score > 1:
    if self.snake_parts[0][1] > self.snake_parts[1][1]:
        self.snake_parts[0] = [self.snake_parts[0][0]+1, self.snake_parts[0][1]-1]
        for i, coord in enumerate(1, self.snake_parts[1:]):
            self.snake_parts[i] = [coord[0], coord[1]+1]
    else:
        self.snake_parts[0] = [self.snake_parts[0][0]+1, self.snake_parts[0][1]+1]
        for i, coord in enumerate(1, self.snake_parts[1:]):
            self.snake_parts[i] = [coord[0], coord[1]+1]
else:
    self.snake_parts[0] = [self.snake_parts[0][0]+1, self.snake_parts[0][1]]