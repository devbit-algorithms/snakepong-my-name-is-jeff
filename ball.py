from canvas import Canvas

class Ball:
    def __init__(self,x,y):
        self._x = x
        self._y = y 

    def x(self):
        return self._x
    
    def y(self):
        return self._y

    def move(self,x,y):
        self._x = x
        self._y = y 

    def render(self, canv):
        
        canv.drawSymbolCanvas(self._x,self._y, "X")
    