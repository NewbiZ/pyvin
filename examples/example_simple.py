import json
import pyvin
import requests

def strategy(game):
    game.board.map.display()
    return 'East'

engine = pyvin.Engine(
    key='bsy9nnr5',
    turns=5,
    map='m1',
    strategy=strategy)

engine.play()
