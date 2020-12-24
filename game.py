from canvas import Canvas
from wall import Wall
from snake import Snake
from tail import Tail
from goal import Goal
from ball import Ball

import threading
from msvcrt import getwch, kbhit

import time
import os


class Game:
    def __init__(self):
        self.canv = Canvas(40,30)
        self.ball = Ball(2, int(self.canv.getHeight()/2) )
        self.direction = "left"
        self.gameover = False
        self.updatecounter = 0
        threading.Thread(target=self.updateDirection).start()
        self.velocityballx = -1
        self.velocitybally = -1
        
        self.walls = []
        self.tails = []
        self.goals = []
        self.snake = Snake(int(self.canv.getWidth()/2),int(self.canv.getHeight()/2))

        self.createWalls()

        self.game_loop()
        
        os.system("clear")
        print("GAME OVER\nPress any key to go back to the terminal.")
        

    def createWalls(self):
        for y in range(self.canv.getHeight()):
            for x in range(self.canv.getWidth()):
                if(x==0 or  y==0 or y == self.canv.getHeight() -1):
                    self.walls.append(Wall(x,y))
                if( x == self.canv.getWidth()-1):
                    self.goals.append(Goal(x,y))



    def game_loop(self):
        counter = 0
        while not self.gameover:
            if counter <= 10:
                self.update()
                counter = 0
            self.render()
            time.sleep(0.2)
            counter += counter

    def update(self):
        
        if (self.updatecounter == 2):
            self.updateBall()
            self.updatecounter = 0
        self.updatecounter += 1
        
        self.updateTail()
        self.updateSnake()
        self.collisionDetection()

    def ballMovement(self):
        self.ball.move(self.ball.x()+self.velocityballx,self.ball.y()+self.velocitybally)
        

    def updateBall(self):
            #hittings with snake!!!
        for tail in self.tails:
            if(tail.x() == self.ball.x() & tail.y() == self.ball.y()):
                self.velocityballx = -(self.velocityballx)

        
        if(self.snake.x()-1 == self.ball.x() & self.snake.y() == self.ball.y()):
                self.velocityballx = -(self.velocityballx)

                
        if (self.ball.x() == 1):
            #ball hitting left wall 
            self.velocityballx = -(self.velocityballx)
        if(self.ball.y() == self.canv.getHeight() -2 or self.ball.y() == 1):
            #ball hitting lower or upper wall
            self.velocitybally = -(self.velocitybally)
        



        self.ballMovement()
        
    def updateDirection(self):
        while not self.gameover:
            key = getwch()
            if (key == "q") & (self.direction is not "right"):
                self.direction = "left" 
            if (key == "d") & (self.direction is not "left"):
                self.direction = "right" 
            if (key == "z") & (self.direction is not "down"):
                self.direction = "up" 
            if (key == "s") & (self.direction is not "up"):
                self.direction = "down" 

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
        taillength = 10
        if len(self.tails) < taillength:
            self.addTailPiece()
        if len(self.tails) >= taillength:
            self.addTailPiece()
            self.deleteLastTailPiece()

    def render(self):
        os.system("clear")
        self.canv.clearCanvas()

        for goal in self.goals:
            goal.render(self.canv)

        for wall in self.walls:
            wall.render(self.canv)

        for tail in self.tails:
            tail.render(self.canv)

        self.snake.render(self.canv,self.direction)

        self.ball.render(self.canv)

        self.canv.outputCanvasTerminal()

    def addTailPiece(self):
        self.tails.append(Tail(self.snake.x(),self.snake.y()))

    def deleteLastTailPiece(self):
        self.tails.pop(0)

    def collisionDetection(self):
        self.collisionWall()
        self.collisionTail()

    def collisionWall(self):
        for wall in self.walls:
            if((wall.x() == self.snake.x()) & (wall.y() == self.snake.y())):
                self.gameover = True

    def collisionTail(self):
        for tail in self.tails:
            if((tail.x() == self.snake.x()) & (tail.y() == self.snake.y())):
                self.gameover = True