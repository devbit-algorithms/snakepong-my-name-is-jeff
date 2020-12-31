from msvcrt import getwch, kbhit
import os
class Settings:
   
        

    def render(self):
        os.system("clear")
        txt = " Here You Can Chose The Settings Of The Game "
        x = txt.center(80, "~")
        print(x)
        txt = " By Pressing \033[1mE\033[0m You Get The Easy Setting "
        x = txt.center(88, "~")
        print(x)
        txt = " By Pressing \033[1mM\033[0m You Get The Medium Setting "
        x = txt.center(88, "~")
        print(x)
        txt = " By Pressing \033[1mH\033[0m You Get The Hard Setting "
        x = txt.center(88, "~")
        print(x)

    def chose_difficulty(self):
        key = getwch()
        if (key == "e"): 
            return  0.5

        if (key == "m"): 
            return  0.2
            
        if (key == "h"): 
            return  0.1
        
        
        
            

