from .board import Board
from .hero import Hero

class Game:
    def __init__(self, response, id):
        self.id = response['id']
        self.turn = response['turn']
        self.maxTurns = response['maxTurns']
        self.heroes = [Hero(h) for h in response['heroes']]
        self.board = Board(response['board'], self.heroes, id)
        self.finished = response['finished']

    def display(self, indent=0):
        disp_indent = lambda n: '    '*n
        print '[Game]'
        print disp_indent(indent) + '    id = %s' % self.id
        print disp_indent(indent) + '    turn = %s' % self.turn
        print disp_indent(indent) + '    maxTurns = %s' % self.maxTurns
        print disp_indent(indent) + '    heroes ='
        for h in self.heroes:
            print disp_indent(indent+1),
            h.display(indent=indent+1)
        print disp_indent(indent) + '    board =',
        self.board.display(indent=indent+1)
        print disp_indent(indent) + '    finished = %s' % self.finished
