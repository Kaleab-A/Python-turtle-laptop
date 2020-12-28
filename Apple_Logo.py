import turtle
from General_Drawing import generalDrawing

turtle.colormode(255)

class AppleLogo(generalDrawing):
    def __init__(self, size, x, y, color1="white", color2=(194,195,197)):
        self.t = turtle.Turtle()
        self.scr = turtle.Screen()
        self.t.hideturtle()
        self.t.speed(0)
        self.size = size
        self.x = x
        self.y = y
        self.color1 = color1
        self.color2 = color2
        self.rgb = [0, 0, 0]

    def gotoInv(self, turtleCursor, x, y):
        return super().gotoInv(turtleCursor, x, y)

    def circle(self, rad, arc=360):
        self.gotoInv(self.t, self.t.position()[0], self.t.position()[1] + rad)
        self.t.circle(-rad, arc)

    def draw(self):
        self.gotoInv(self.t, self.x, self.y)
        self.t.color(self.color1)
        self.t.begin_fill()
        self.t.setheading(90)
        self.t.circle(-self.size , 90)
        self.t.setheading(-90)
        self.t.circle(-self.size, 90)
        self.t.setheading(0)
        self.t.end_fill()
        
        self.gotoInv(self.t, self.t.position()[0], self.t.position()[1]-self.size/2)
        self.t.begin_fill()
        self.t.setheading(180-45)
        self.t.circle(self.size, 135)
        for i in range(0, 50, 2):
            self.t.setheading(270+i)
            self.t.forward(self.size/10)

        dis = self.size / 2.2
        self.t.setheading(0-45)
        self.t.circle(dis, 90)
        self.t.circle(-dis, 90)
        self.t.circle(dis, 90)

        self.t.setheading(44)
            
        pos = self.t.heading()
        for i in range(0, 50, 2):
            self.t.forward(self.size/10)
            self.t.setheading(pos+i)
            
        self.t.setheading(180-90)
        self.t.circle(self.size, 135)
        
        self.t.circle(-self.size / 3, 90)
        self.t.end_fill()

        self.t.penup()
        self.t.setheading(0)
        self.t.forward(self.size*1.3)
        self.t.setheading(270)
        self.t.forward(self.size)
        self.t.pendown()
        self.t.color(self.color2)
        self.t.begin_fill()
        self.t.circle(self.size)
        self.t.end_fill()

    def clear(self):
        return self.t.clear()

if __name__ == "__main__":
    apple = AppleLogo( 20, 0, 200, "green","white") # Col chaneg
    apple.draw()
    apple.scr.mainloop()

    