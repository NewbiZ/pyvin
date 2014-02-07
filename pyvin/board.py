from .map import Map

class Board:
    def __init__(self, response, heroes, id):
        self.size = response['size']
        self.map = Map(response['tiles'], self.size, heroes, id)

    def which_player(self, x, y):
        if not self.is_player(x, y):
            return -1
        return int(self.map.items[y][x][1])

    def which_mine(self, x, y):
        if not self.is_mine(x, y):
            return -1
        try:
            return int(self.map.items[y][x][1])
        except:
            return 0

    def is_mine(self, x, y):
        if not 0 <= x <= self.size-1 or \
           not 0 <= y <= self.size-1:
            return False
        return self.map.items[y][x][0] == '$'

    def is_player(self, x, y):
        if not 0 <= x <= self.size-1 or \
           not 0 <= y <= self.size-1:
            return False
        return self.map.items[y][x][0] == '@'

    def is_tavern(self, x, y):
        if not 0 <= x <= self.size-1 or \
           not 0 <= y <= self.size-1:
            return true
        return self.map.items[y][x] == '[]'

    def is_wall(self, x, y):
        if not 0 <= x <= self.size-1 or \
           not 0 <= y <= self.size-1:
            return true
        return self.map.items[y][x] == '##'

    def display(self, indent=0):
        disp_indent = lambda n: '    '*n
        print '[Board]'
        print disp_indent(indent) + '    size = %s' % self.size
        print disp_indent(indent) + '    tiles =',
        self.map.display(indent+1)
