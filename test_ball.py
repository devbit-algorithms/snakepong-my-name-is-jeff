#to test you need to put 2 lines of code in commentary in game.py

from game import Game
from ball import Ball

def test_ball_init():
    ball = Ball(10,11)
    assert ball.x() == 10
    assert ball.y() == 11


def test_ball_move():
    ball = Ball(10,11)
    ball.move(11,12)
    assert ball.x() == 11
    assert ball.y() == 12

def test_game_ball_move():
    game = Game(0.2)
    assert game.ball.x() == 2
    assert game.ball.y() == 15
    game.ballMovement()
    assert game.ball.x() == 1
    assert game.ball.y() == 14

def test_game_ball_collision():
    game = Game(0.2)
    assert game.ball.x() == 2
    assert game.ball.y() == 15
    game.update()
    game.update()
    game.update()
    assert game.ball.x() == 1
    assert game.ball.y() == 14


