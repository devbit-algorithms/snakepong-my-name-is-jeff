from canvas import Canvas
from wall import Wall

class Game:
    def __init__(self):
        self.canv = Canvas(10,10)
        self.walls = []



        self.createWalls()
        self.render()
        self.canv.outputCanvasTerminal()

    def createWalls(self):
        for x in range(self.canv.getWidth()):
            for y in range(self.canv.getHeight()):
                if(x==0 or x == self.canv.getWidth() - 1 or y==0 or y == self.canv.getHeight() -1):
                    self.walls.append(Wall(x,y))

    def render(self):
        for wall in self.walls:
            wall.render(self.canv)

