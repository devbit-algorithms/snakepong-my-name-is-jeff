from wallsmenu import Menuwall
from canvas import Canvas
import threading
from msvcrt import getwch, kbhit
import os
from game import Game
from settings import Settings
import time


class Menu:
    def __init__(self):
        self.canv = Canvas(40,30)
        threading.Thread(target=self.chose).start()
        self.gameover = False
        self.walls = []
        self.createMenuWalls()
        self.Menu_loop()
        
        
    def createMenuWalls(self):
        for y in range(self.canv.getHeight()):
            for x in range(self.canv.getWidth()):
                if(x==0 or  y==0 or y == self.canv.getHeight() - 1 or x == self.canv.getWidth()-1):
                    self.walls.append(Menuwall(x,y) )


    def Menu_loop(self):
        while not self.gameover:
            self.render()
            self.chose()


    def render(self):
        os.system("clear")
        txt = "Welcome To The Snake Game Made By Seppe En Robin"
        x = txt.center(80, "~")
        print(x)
        txt = "By Pressing \033[1mS\033[0m you can choose the Settings Hard-Medium-Easy"
        x = txt.center(88, "~")
        print(x)
        txt = "By Pressing \033[1mP\033[0m You Advance To The Game"
        x = txt.center(88, "~")
        print(x)
    
    def chose(self):
        while not self.gameover:
            key = getwch()
            if (key == "s"): 
                Settings()
                self.gameover = True
            if (key == "p"): 
                Game()
                self.gameover = True
            

        
        


        
        
                


        
            
