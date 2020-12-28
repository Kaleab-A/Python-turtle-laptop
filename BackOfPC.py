import turtle
from Apple_Logo import AppleLogo
from General_Drawing import generalDrawing

t = turtle.Turtle()
scr = turtle.Screen()
t.hideturtle()
t.pensize(4)
turtle.colormode(255)
scr.bgcolor("light yellow")

class PC_BACK(generalDrawing):
    def __init__(self, pos1, pos2, pos3, pos4):
        t.speed(0)
        t.left(90)
        self.pos1 = pos1
        self.pos2 = pos2
        self.pos3 = pos3
        self.pos4 = pos4

        self.y_diff = self.pos4[1] - self.pos1[1]
        
        self.topLeft = (pos1[0] + 18, pos1[1] + self.y_diff - 8)
        self.topRight = (pos2[0] - 35, pos2[1] + self.y_diff - 9)
        self.bottomRight = (pos3[0] + 30 , -2 * pos3[1] + self.y_diff + 30)
        self.bottomLeft = (pos4[0] - 40,  -2 * pos4[1] + self.y_diff + 15)
        self.appleLOGO = AppleLogo(20, (self.topLeft[0] + self.topRight[0]) / 2, -110) # On the back of the macintosh
        generalDrawing.__init__(self, t)
        
    def gotoInv(self, turtleCursor, x, y):
        return super().gotoInv(turtleCursor, x, y)
    
    def draw_quad(self, pos, pos1, pos2, pos3, pos4, curve=0):
            t.hideturtle()
            self.gotoInv(t, pos1[0], pos1[1])
            t.circle(curve, 90)
            t.goto((pos2[0], pos2[1]))
            t.circle(curve, 90)    
            t.goto((pos3[0] , pos3[1]))
            t.circle(curve, 90) 
            t.goto((pos4[0], pos4[1]))
            t.circle(curve, 90)  
            t.goto((pos1[0], pos1[1]))

    def draw(self):
        self.drawKeyB()
        self.appleLOGO.draw()

    def clear(self):
        t.clear()
        self.appleLOGO.clear()
        
    def drawKeyB(self):
        t.color((218,217,222))
        t.begin_fill()
        self.draw_quad(self.topLeft, self.topLeft, self.topRight, (self.bottomRight[0], self.bottomRight[1]-10), (self.bottomLeft[0], self.bottomLeft[1]-10), -5)
        t.end_fill()

        t.color((147,151,152))
        t.begin_fill()
        self.draw_quad(self.topLeft, self.topLeft, (self.topRight[0]+2, self.topRight[1]), (self.bottomRight[0]+2, self.bottomRight[1]), self.bottomLeft, -5)
        t.end_fill()

        t.color((147,151,152))
        t.begin_fill()
        self.draw_quad(self.topLeft, self.topLeft, self.topRight, (self.bottomRight[0], self.bottomRight[1]-2), (self.bottomLeft[0], self.bottomLeft[1]-2), -5)
        t.end_fill()
        
        t.color((194,195,197))
        t.begin_fill()
        self.draw_quad(self.topLeft, self.topLeft, self.topRight, self.bottomRight, self.bottomLeft, -5)
        t.end_fill()


        t.pensize(2)
        t.setheading(0)
        t.color((34,29,29))
        self.gotoInv(t, 230, -267)
        t.forward(15)
        t.setheading(90)
        t.pensize(4)

# scr.mainloop()