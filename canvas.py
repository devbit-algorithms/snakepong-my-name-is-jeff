
class Canvas:
    def __init__(self, width,height):
        self.width = width
        self.height = height
        self.screen = [['' for i in range(height)] for j in range(width)] 
        self.clearCanvas()
        
    def clearCanvas(self):
        for y in range  (0,self.height):
            for x in range (0,self.width):
                self.screen[x][y] = ' '

    def drawSymbolCanvas(self, x, y, symbol):
        self.screen[x][y] = symbol
    
    def outputCanvasTerminal(self):
        for y in range (0,self.height):
            for x in range (0,self.width):
                print(self.screen[x][y],end = " ")
            print()
        print()

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height