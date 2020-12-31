from canvas import Canvas
import threading
from msvcrt import getwch, kbhit
import os
from game import Game
from settings import Settings
import time


class Menu:
    def __init__(self):
        self.gameover = False
        self.timeforgame = 0.2
        self.settings = Settings()
        self.Menu_loop()

    def Menu_loop(self):
        while not self.gameover:
            self.render()
            self.chose()


    def render(self):
        os.system("clear")
        txt = " Welcome To The Snake Game Made By Seppe En Robin "
        x = txt.center(80, "~")
        print(x)
        txt = " By Pressing \033[1mS\033[0m you can choose the Settings Hard-Medium-Easy "
        x = txt.center(88, "~")
        print(x)
        txt = " By Pressing \033[1mP\033[0m You Advance To The Game "
        x = txt.center(88, "~")
        print(x)
    
    def chose(self):
        key = getwch()
        if (key == "s"): 
            self.settings.render()
            self.timeforgame = self.settings.chose_difficulty()
            self.render()
        if (key == "p"): 
            Game(self.timeforgame)
            self.gameover = True
            

        
        


        
        
                


        
            
