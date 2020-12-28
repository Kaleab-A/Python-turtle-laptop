import turtle
from os.path import expanduser
from General_Drawing import generalDrawing
# from tkinter import PhotoImage

class Image(generalDrawing):
    def __init__(self, imagePath, xPos, yPos):
        self.t = turtle.Turtle()
        self.scr = turtle.Screen()
        self.imagePath =  expanduser(imagePath)
        self.x = xPos
        self.y = yPos

    def gotoInv(self, turtleCursor, x, y):
        return super().gotoInv(turtleCursor, x, y)

    def draw(self):
        self.gotoInv(self.t, self.x, self.y)
        self.scr.addshape(self.imagePath)
        self.t.showturtle()
        self.t.shape(self.imagePath)
        self.t.showturtle()

    def clear(self):
        pass

if __name__ == "__main__":
    # powerButton = Image(".//Images//pig.gif", 300, 100)
    # powerButton.draw()
    # powerButton.scr.mainloop()
    wallpaper = Image(".//Images//screen1.gif", 0, 0)
    wallpaper.draw()
    wallpaper.scr.mainloop()