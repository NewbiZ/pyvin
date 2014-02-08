Pyvin: Python library to play Vindinium
---------------------------------------

`pyvin` is a simple python package to abstract most of the boilerplate required to play Vindinium. The only thing you have to do is to create a function taking a `game` parameter and returning the move you want to play.

From [Vindinium website](http://vindinium.org)
> Vindinium is an Artificial Intelligence programming challenge. You have to take the control of a legendary hero using the programming language of your choice. You will fight with other AI for a predetermined number of turns and the hero with the greatest amount of gold will win.

Example:
    import pyvin
    
    def strategy(game):
        game.board.map.display()
        return 'East'
    
    engine = pyvin.Engine(
        key='*******',
        turns=5,
        map='m1',
        strategy=strategy)
    
    engine.play()

FAQ
---
Only training mode is possible at the moment

Authors
-------
- Aurelien Vallee <vallee.aurelien@gmail.com>
