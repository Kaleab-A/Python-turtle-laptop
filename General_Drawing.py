import turtle

class generalDrawing:
    def __init__(self, t):
        self.t = t
        self.t.hideturtle()

    def gotoInv(self, turtleCursor, x, y):
        self.t.hideturtle()
        turtleCursor.penup()
        turtleCursor.goto(x, y)
        turtleCursor.pendown()

    def drawQuadrilateral (self, topLeft, topRight, bottomRight, bottomLeft, curve=0, lineColor=None, colorFill=None ):
        self.t.hideturtle()
        startHeading = self.t.heading()
        self.t.setheading(90)
        if lineColor != None and colorFill == None:
            colorFill = lineColor
        if lineColor == None:
            lineColor = "black"
        if colorFill == None:
            colorFill = "white"
        self.gotoInv(self.t, topLeft[0], topLeft[1] )
        vertices = [topRight, bottomRight, bottomLeft, topLeft ]
        self.t.color(lineColor, colorFill)
        self.t.begin_fill()
        for vertex in vertices:
            self.t.circle(-curve, 90)
            self.t.goto(vertex[0], vertex[1])
        self.t.end_fill()
        self.t.setheading(startHeading)