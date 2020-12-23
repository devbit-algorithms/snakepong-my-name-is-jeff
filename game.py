from canvas import Canvas
from wall import Wall
from snake import Snake
from tail import Tail

import threading
from msvcrt import getwch, kbhit

import time
import os


class Game:
    def __init__(self):
        self.canv = Canvas(20,20)
        self.direction = "right"
        keyinputthread = threading.Thread(target=self.updateDirection)
        keyinputthread.start()

        self.walls = []
        self.tails = []
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
        self.updateTail()
        self.updateSnake()
        

    def updateDirection(self):
        while True:
            key = getwch()
            if key == "q":
                self.direction = "left" #left
            if key == "d":
                self.direction = "right" #right
            if key == "z":
                self.direction = "up" #down
            if key == "s":
                self.direction = "down" #up

    def updateSnake(self):
        
        if self.direction =="left":
            self.snake.move(self.snake.x()-1,self.snake.y()) #left
        if self.direction == "right":
            self.snake.move(self.snake.x()+1,self.snake.y()) #right
        if self.direction == "up":
            self.snake.move(self.snake.x(),self.snake.y()-1) #right
        if self.direction == "down":
            self.snake.move(self.snake.x(),self.snake.y()+1) #right

    def updateTail(self):
        taillength = 7
        if len(self.tails) < taillength:
            self.addTailPiece()
        if len(self.tails) >= taillength:
            self.addTailPiece()
            self.deleteLastTailPiece()


        

    def render(self):
        os.system("clear")
        self.canv.clearCanvas()
        for wall in self.walls:
            wall.render(self.canv)

        for tail in self.tails:
            tail.render(self.canv)

        self.snake.render(self.canv)

        self.canv.outputCanvasTerminal()

    def addTailPiece(self):
        self.tails.append(Tail(self.snake.x(),self.snake.y()))

    def deleteLastTailPiece(self):
        self.tails.pop(0)

