
class Canvas:
    def __init__(self, width,height):
        self.width = width
        self.height = height
        self.screen = [['' for i in range(width)] for j in range(height)] 
        
    def clearCanvas(self):
        for x in self.width:
            for y in self.height:
                self.screen[x][y] = ' '

    def drawSymbolCanvas(self, x, y, symbol):
        self.screen[x][y] = symbol
    
    def outputCanvasTerminal(self):
        for x in self.width:
            for y in self.width:
                print(self.screen[x][y])
        print("\n")