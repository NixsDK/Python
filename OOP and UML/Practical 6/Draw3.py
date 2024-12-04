import turtle

class Canvas:
    def __init__(self, w, h):
        self.__visibleObjects = []   #list of shapes to draw
        self.__turtle = turtle.Turtle()
        self.__screen = turtle.Screen()
        self.__screen.setup(width = w, height = h)
        self.__turtle.hideturtle()

    def drawAll(self):
        self.__turtle.reset()
        self.__turtle.up()
        self.__screen.tracer(0)
        for shape in self.__visibleObjects: #draw all shapes in order
            shape._draw(self.__turtle)
        self.__screen.tracer(1)
        self.__turtle.hideturtle()

    def addShape(self, shape):
        self.__visibleObjects.append(shape)

    def draw(self, gObject):
        gObject.setCanvas(self)
        gObject.setVisible(True)
        self.__turtle.up()
        self.__screen.tracer(0)
        gObject._draw(self.__turtle)
        self.__screen.tracer(1)
        self.addShape(gObject)

from abc import *
class GeometricObject(ABC):
    def __init__(self):
        self.__lineColor = 'black'
        self.__lineWidth = 1
        self.__visible = False
        self.__myCanvas = None

    def setColor(self, color):  #modified to redraw visible shapes
        self.__lineColor = color
        if self.__visible:
            self.__myCanvas.drawAll()

    def setWidth(self, width):  #modified to redraw visible shapes
        self.__lineWidth = width
        if self.__visible:
            self.__myCanvas.drawAll()

    def getColor(self):
        return self.__lineColor

    def getWidth(self):
        return self.__lineWidth

    @abstractmethod
    def _draw(self):
        pass

    def setVisible(self, vFlag):
        self.__visible = vFlag

    def getVisible(self):
        return self.__visible

    def setCanvas(self, theCanvas):
        self.__myCanvas = theCanvas

    def getCanvas(self):
        return self.__myCanvas

class Point(GeometricObject):
    def __init__(self, x, y):
        super().__init__()
        self.coords = (x, y)

    def getCoord(self):
        return self.coords

    def getX(self):
        return self.coords[0]

    def getY(self):
        return self.coords[1]

    def _draw(self, turtle):
        turtle.goto(self.__x, self.__y)
       # turtle.dot(self.__lineWidth, self.__lineColor)
        turtle.dot(self.getWidth(), self.getColor())

class Line(GeometricObject):
    def __init__(self, p1, p2):
        super().__init__()
        self.__p1 = p1
        self.__p2 = p2

    def getP1(self):
        return self.__p1

    def getP2(self):
        return self.__p2

    def _draw(self, turtle):
        turtle.color(self.getColor())
        turtle.width(self.getWidth())
        turtle.up()
        turtle.goto(self.__p1.getCoord())
        turtle.down()
        turtle.goto(self.__p2.getCoord())
    
    def getColor(self):
        return super().getColor()

class Rectangle(GeometricObject):
    def __init__(self, x, y, width, height=None):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height or width

    def _draw(self, turtle):
        turtle.up()
        turtle.goto(self.x, self.y)
        turtle.down()
        turtle.color(self.getColor())
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(self.width)
            turtle.left(90)
            turtle.forward(self.height)
            turtle.left(90)
        turtle.end_fill()


class Triangle(GeometricObject):
    def __init__(self, x, y, side_length, height=None):
        super().__init__()
        self.x = x
        self.y = y
        self.side_length = side_length
        self.height = height or (self.side_length * (3 ** 0.5)) / 2 

    def _draw(self, turtle):
        turtle.up()
        turtle.goto(self.x, self.y)
        turtle.down()
        turtle.color(self.getColor())
        turtle.begin_fill()
        turtle.goto(self.x + self.side_length / 2, self.y + self.height)
        turtle.goto(self.x + self.side_length, self.y)
        turtle.goto(self.x, self.y)
        turtle.end_fill()


class Circle(GeometricObject):
    def __init__(self, x, y, radius):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius

    def _draw(self, turtle):
        turtle.up()
        turtle.goto(self.x, self.y - self.radius)
        turtle.down()
        turtle.color(self.getColor())
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.end_fill()


def draw_house():
    canvas = Canvas(800, 600)

    # zime majas main dalu
    house_body = Rectangle(-50, -100, 200, 150)
    house_body.setColor("blue")
    canvas.draw(house_body)

    # zime jumta outline
    roof_outline = Triangle(-50, 50, 200, 120)
    roof_outline.setColor("black")
    roof_outline.setWidth(2)  # outlaina platums
    canvas.draw(roof_outline)

    # zime durvis
    door = Rectangle(-15, -100, 30, 75)
    door.setColor("red")
    canvas.draw(door)

    # zime sauli 
    sun = Circle(170, 170, 30)
    sun.setColor("yellow")
    canvas.draw(sun)

    #patira ekranu atve
    turtle.done()

def test2():
    myCanvas = Canvas(500, 500)
    line1 = Line(Point(-100, -100), Point(100, 100))
    line2 = Line(Point(-100, 100), Point(100, -100))
    line1.setWidth(4)    
    myCanvas.draw(line1)
    myCanvas.draw(line2)
    line1.setColor('red')
    line2.setWidth(4)
    
    turtle.done()
    
# palaiz programmu
draw_house()
#test2()
