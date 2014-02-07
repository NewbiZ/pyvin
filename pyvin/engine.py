from .game import Game

class Engine:
    def __init__(self, response):
        self.token = response['token']
        self.viewUrl = response['viewUrl']
        self.playUrl = response['playUrl']
        self.id = response['hero']['id']
        self.game = Game(response['game'], self.id)

    def display(self, indent=0):
        disp_indent = lambda n: '    '*n
        print '[Engine]'
        print disp_indent(indent) + '    token = %s' % self.token
        print disp_indent(indent) + '    playUrl = %s' % self.playUrl
        print disp_indent(indent) + '    token = %s' % self.viewUrl
        print disp_indent(indent) + '    id = %s' % self.id
        print disp_indent(indent) + '    game =',
        self.game.display(indent=indent+1)
