from canvas import Canvas

class Snake:
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

    def render(self, canv,direction):
        if direction == "left":
            canv.drawSymbolCanvas(self._x,self._y, "<")
        if direction == "right":
            canv.drawSymbolCanvas(self._x,self._y, ">")
        if direction == "up":
            canv.drawSymbolCanvas(self._x,self._y, "^")
        if direction == "down":
            canv.drawSymbolCanvas(self._x,self._y, "v")