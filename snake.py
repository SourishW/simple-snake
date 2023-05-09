from main import UP, DOWN, LEFT, RIGHT, names
import random

def update_location(node, direction):
    node_copy = node.copy()
    if (direction == UP):
        node_copy[1]+=1
    if (direction == DOWN):
        node_copy[1]-=1
    if (direction == LEFT):
        node_copy[0]-=1
    if (direction == RIGHT):
        node_copy[0]+=1
    return node_copy

class Snake:

    def __init__(self, board_width, board_height):
        self.board_width = board_width
        self.board_height = board_height
        self.direction = UP
        self.nodes = [[int(board_width/2), int(board_height/2)]]
        self.grow = False
        
    def set_direction(self, direction):
        if ([self.direction, direction] not in [[UP, DOWN], [DOWN, UP], [LEFT, RIGHT], [RIGHT, LEFT]]):
            self.direction = direction

    def grow_one(self):
        self.grow = True


    def move(self):
        # everything moves up one spot, the last node gets deleted, and the new location is updated
        self.nodes.insert(0, update_location(self.nodes[0], self.direction))
        if (not self.grow):
            self.nodes.pop(-1)
        self.grow = False
    
    
    def game_over(self):
        head = self.nodes[0]

        # check self collision
        for node in self.nodes[1:]:
            if head[0] == node[0] and head[1] == node[1]:
                return True
            
        # check boundary collision
        if (head[0]<0 or head[0]>=self.board_width):
            return True
        if (head[1]<0 or head[1]>=self.board_height):
            return True
        return False
    

    def __str__(self):
        snake_str = ""
        for node in self.nodes:
            snake_str += f"({node[0]}, {node[1]}) -> "
        snake_str = snake_str[:-4] # remove the last arrow
        snake_str = "Direction = " + names[self.direction] + ", " +snake_str
        return snake_str


if __name__ == "__main__":
    snake = Snake(15, 15)
    while(not snake.game_over()):
        print (str(snake))
        if (random.randint(0, 2)==1):
            snake.grow_one()
        snake.set_direction(random.randint(0, 3))
        snake.move()
    print (str(snake))
