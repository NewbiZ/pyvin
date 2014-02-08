from .game import Game

import json
import requests

class Engine:
    def __init__(self, key='abcd', turns=300, map='m1', strategy=lambda game: 'Stay'):
        self.key = key
        self.turns = turns
        self.map = map
        self.strategy = strategy

    def play(self):
        response = json.loads(requests.post('http://vindinium.org/api/training', {
            'key': self.key,
            'turns': self.turns,
            'map': self.map,
        }).text)

        self.update(response)

        print 'Game started...'

        while not self.game.finished:
            action = self.strategy(self.game)
            response = json.loads(requests.post(self.playUrl, {
                'key': self.key,
                'dir': action
            }).text)
            self.update(response)

        print 'Game finished.\n'

        self.display()

    def update(self, response):
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
        print disp_indent(indent) + '    viewUrl = %s' % self.viewUrl
        print disp_indent(indent) + '    token = %s' % self.viewUrl
        print disp_indent(indent) + '    id = %s' % self.id
        print disp_indent(indent) + '    game =',
        self.game.display(indent=indent+1)
