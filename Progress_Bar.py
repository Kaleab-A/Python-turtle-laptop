import turtle
from  General_Drawing import generalDrawing
import time

class ProgressBar(generalDrawing):
    def __init__(self, speed, posX, posY, width, height, bgcolor, color):
        self.speed = speed
        self.width = width
        self.height = height 
        self.bgcolor = bgcolor
        self.color = color
        self.t = turtle.Turtle()
        self.scr = turtle.Screen()
        self.posX = posX
        self.posY = posY
        self.scr = turtle.Screen()
        self.t.speed(0)
        self.start = time.time()

    def gotoInv(self, turtleCursor, x, y):
        return super().gotoInv(turtleCursor, x, y)

    def draw(self):
        self.t.hideturtle()
        self.gotoInv(self.t, self.posX, self.posY)
        self.t.setheading(0)

        # Drawing background of the progress bar
        self.t.color(self.bgcolor)
        self.t.pensize(self.height)
        self.t.backward(self.width)
        # self.t.begin_fill()
        # for i in range(2): # TODO Convert to simple forward to solve height increasing when refreshing
        #     self.t.right(90)
        #     self.t.forward(self.height)
        #     self.t.right(90)
        #     self.t.forward(self.width)
        # self.t.end_fill()

        # Drawing the moving progress bar
        self.scr.tracer(True)
        self.t.color(self.color)
        self.gotoInv(self.t, self.posX - self.width, self.posY )
        self.t.pensize(self.height)
        for i in range(self.width):
            self.t.forward(1)
            time.sleep(1/(100*self.speed))
        self.scr.tracer(False)

    def clear(self):
        self.scr.tracer(False)
        self.t.clear()

if __name__ == "__main__":
    obj = ProgressBar(10, 0, 0, 200, 20, "grey", "black")
    obj.draw()
    src = turtle.Screen()
    end = time.time()
    print("Time Taken:", end - obj.start)
    src.mainloop()