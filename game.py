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
    def __init__(self, time):
        
        self.time = time
        self.canv = Canvas(40,30)
        self.ball = Ball(2, int(self.canv.getHeight()/2) )
        self.direction = "left"
        self.gameover = False
        self.updatecounter = 0
        self.score = 0
        threading.Thread(target=self.updateDirection).start()
        self.velocityballx = -1
        self.velocitybally = -1
        self.receivedInput = False
        
        self.walls = []
        self.tails = []
        self.goals = []
        self.snake = Snake(int(self.canv.getWidth()/2),int(self.canv.getHeight()/2))
        self.createWalls()
        self.game_loop()
        os.system("clear")
        print("GAME OVER\nYour score was: " + str(self.score)+ "\nPress any key to go back to the terminal.\n")
        

    def createWalls(self):
        for y in range(self.canv.getHeight()):
            for x in range(self.canv.getWidth()):
                if(x==0 or  y==0 or y == self.canv.getHeight() -1):
                    self.walls.append(Wall(x,y))
                if( x == self.canv.getWidth()-1):
                    self.goals.append(Goal(x,y))



    def game_loop(self):
        
        while not self.gameover:
            
            self.update()
                
            self.render()
            time.sleep(self.time)
            

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
        for tail in self.tails:
            if((tail.y() == self.ball.y()) & ((tail.x()-1 == self.ball.x()) or (tail.x()-1 == self.ball.x())) and self.velocityballx > 0):
                self.velocityballx = -(self.velocityballx)
                self.score += 1

        if(self.snake.x()-1 == self.ball.x() & self.snake.y() == self.ball.y()):
            self.velocityballx = -(self.velocityballx)
            self.score += 1

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
            if (key == "q") & (self.direction is not "right") & (not self.receivedInput) :
                self.direction = "left"
                self.receivedInput = True
            if (key == "d") & (self.direction is not "left") & (not self.receivedInput):
                self.direction = "right"
                self.receivedInput = True
            if (key == "z") & (self.direction is not "down") & (not self.receivedInput):
                self.direction = "up"
                self.receivedInput = True
            if (key == "s") & (self.direction is not "up") & (not self.receivedInput):
                self.direction = "down"
                self.receivedInput = True


    def updateSnake(self):
        
        if self.direction =="left":
            self.snake.move(self.snake.x()-1,self.snake.y()) #left
        if self.direction == "right":
            self.snake.move(self.snake.x()+1,self.snake.y()) #right
        if self.direction == "up":
            self.snake.move(self.snake.x(),self.snake.y()-1) #right
        if self.direction == "down":
            self.snake.move(self.snake.x(),self.snake.y()+1) #right
        self.receivedInput = False
        
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
        print("Score: " + str(self.score))

    def addTailPiece(self):
        self.tails.append(Tail(self.snake.x(),self.snake.y()))

    def deleteLastTailPiece(self):
        self.tails.pop(0)

    def collisionDetection(self):
        self.collisionWall()
        self.collisionTail()
        self.collisionGoal()

    def collisionWall(self):
        for wall in self.walls:
            if((wall.x() == self.snake.x()) & (wall.y() == self.snake.y())):
                self.gameover = True

    def collisionTail(self):
        for tail in self.tails:
            if((tail.x() == self.snake.x()) & (tail.y() == self.snake.y())):
                self.gameover = True

    def collisionGoal(self):
        #ball with goal:
        if(self.ball.x() == self.canv.getWidth()-1):
            self.gameover = True
        
        #snake with goal:
        if(self.snake.x() == self.canv.getWidth()-1):
            self.gameover = True
        