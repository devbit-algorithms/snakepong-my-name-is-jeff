import time
import threading
from game import Game

from msvcrt import getwch, kbhit
import os
class Settings:
    def __init__(self):
        
        self.difficultychosen = False
        threading.Thread(target=self.chose_difficulty).start()
        self.gameover = False
        self.settingsLoop()
    
    def settingsLoop(self):
        while not self.gameover:
            self.render()
            self.chose_difficulty()
        if(self.gameover == True):
            Game()
        
        

    def render(self):
        os.system("clear")
        txt = "Here You Can Chose The Settings Of The Game"
        x = txt.center(80, "~")
        print(x)
        txt = "By Pressing \033[1mE\033[0m You Get The Easy Setting"
        x = txt.center(88, "~")
        print(x)
        txt = "By Pressing \033[1mM\033[0m You Get The Medium Setting"
        x = txt.center(88, "~")
        print(x)
        txt = "By Pressing \033[1mH\033[0m You Get The Hard Setting"
        x = txt.center(88, "~")
        print(x)

    def chose_difficulty(self):
        while not self.gameover:
            key = getwch()
            if (key == "e"): 
                self.Easy = time.sleep(0.5)
                Time_difficulty = self.Easy
                print("E works")
                self.gameover = True
                self.difficultychosen = True
                
            if (key == "m"): 
                self.Medium = time.sleep(0.2)
                Time_difficulty = self.Medium
                print("M works")
                self.gameover = True
                self.difficultychosen = True
            if (key == "h"): 
                self.Hard = time.sleep(0.1)
                Time_difficulty = self.Hard
                print("H works")
                self.gameover = True
                self.difficultychosen = True
        return Time_difficulty
        
        
            

