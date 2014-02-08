import json
import pyvin
import requests

def strategy(game):
    game.board.map.display()
    return 'East'

engine = pyvin.Engine(
    key='*******',
    turns=5,
    map='m1',
    strategy=strategy)

engine.play()
