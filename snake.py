from main import UP, DOWN, LEFT, RIGHT

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

        self.nodes = [[board_width/2, board_height/2]]
        
    def set_direction(self, direction):
        if ([self.direction, direction] not in [[UP, DOWN], [DOWN, UP], [LEFT, RIGHT], [RIGHT, LEFT]]):
            self.direction = direction

    def move(self):
        self.nodes.pop(-1)
        self.nodes.insert(0, update_location(self.nodes[0], self.direction))
    
    def check_game_over(self):
        head = self.nodes[0]
        for node in self.nodes[1:]:
            if head[0] == node[0] and head[1] == node[1]:
                return False
        
