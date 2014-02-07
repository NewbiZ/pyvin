import json
import pyvin
import requests

response = json.loads(open('response.json').read())

engine = pyvin.Engine(response)

engine.game.board.map.display()
