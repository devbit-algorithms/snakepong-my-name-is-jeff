#to test you need to put 2 lines of code in commentary in game.py
from snake import Snake
from game import Game


def test_snakeinit():
    snake = Snake(10,11)
    assert snake.x() == 10
    assert snake.y() == 11

def test_snakemove():
    snake = Snake(5,10)
    assert snake.x() == 5
    assert snake.y() == 10
    snake.move(11,12)
    assert snake.x() == 11
    assert snake.y() == 12

def test_game_snake_move():
    game = Game(0.2)
    assert game.snake.x() == 20
    assert game.snake.y() == 15 # intitialize!
    game.direction = "left"
    game.updateSnake()
    assert game.snake.x() == 19
    assert game.snake.y() == 15 
    game.direction = "right"
    game.updateSnake()
    assert game.snake.x() == 20
    assert game.snake.y() == 15 
    game.direction = "up"
    game.updateSnake()
    assert game.snake.x() == 20
    assert game.snake.y() == 14 
    game.direction = "down"
    game.updateSnake()
    assert game.snake.x() == 20
    assert game.snake.y() == 15 

def test_snake_wall_collision():
    game = Game(0.2)
    assert game.snake.x() == 20
    assert game.snake.y() == 15 # intitialize!
    game.snake.move(2,10)
    game.direction = "left"
    game.updateSnake()
    game.collisionDetection()
    assert game.gameover == False
    game.updateSnake()
    game.collisionDetection()
    assert game.gameover == True
