
class Canvas:
    def __init__(self, width,height):
        self.width = width
        self.height = height
        self.screen = [['' for i in range(width)] for j in range(height)] 
        self.clearCanvas()
        
    def clearCanvas(self):
        for x in range  (0,self.width):
            for y in range (0,self.height):
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