from canvas import Canvas
from wall import Wall
from snake import Snake
import time
import os


class Game:
    def __init__(self):


        self.canv = Canvas(20,20)
        
        self.walls = []
        self.snake = Snake(int(self.canv.getWidth()/2),int(self.canv.getHeight()/2))

        self.createWalls()

        self.game_loop()
        

    def createWalls(self):
        for y in range(self.canv.getHeight()):
            for x in range(self.canv.getWidth()):
                if(x==0 or x == self.canv.getWidth() - 1 or y==0 or y == self.canv.getHeight() -1):
                    self.walls.append(Wall(x,y))


    def game_loop(self):
        while True:
            self.update()
            self.render()
            time.sleep(1)
            
            
            
            


    def update(self):
        self.updateSnake()
        

    def updateSnake(self):
        self.snake.move(self.snake.x()-1,self.snake.y()) 
        self.snake.move(self.snake.x(),self.snake.y()-1) 
    def render(self):
        os.system("clear")
        self.canv.clearCanvas()
        for wall in self.walls:
            wall.render(self.canv)

        self.snake.render(self.canv)

        self.canv.outputCanvasTerminal()


