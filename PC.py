import turtle
from BackOfPC import PC_BACK
from Apple_Logo import AppleLogo
from General_Drawing import generalDrawing
from Progress_Bar import ProgressBar
import time
from Image import Image

turtle.colormode(255)

class PC(generalDrawing):
    def __init__(self, size, topLeft, topRight, bottomRight, bottomLeft ):
        # Initializing Turtle object 
        self.t = turtle.Turtle(visible=False)
        self.scr = turtle.Screen()

        self.t.pensize(4)
        self.t.hideturtle()
        self.scr.tracer(False)
        self.scr.bgcolor("light yellow")

        self.scale = size
        self.topLeft = topLeft
        self.topRight = [topRight[0] * self.scale, topRight[1]]
        self.bottomLeft = [bottomLeft[0], bottomLeft[1] * self.scale]
        self.bottomRight = [bottomRight[0] * self.scale, bottomRight[1] * self.scale]
        self.pcScreenDimension = [[self.topLeft[0], self.topLeft[1]-5], [self.topRight[0], self.topRight[1]-5], self.bottomRight, self.bottomLeft]
        self.screenColor = (6, 6, 8)
        self.colorMap = {"lightGrey": (188, 188, 188), "nearBlack": (6, 6, 8)}
        self.letters = [
                ["esc", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10","F11", "F12", "-->>"],
                ["~~", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0","--", "+", "    <<---"],
                ["-->|", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P","[", "]", "   "],
                ["CAPS", "A", "S", "D", "F", "G", "H", "J", "K", "L", ":",'"', "\\", "<<-|"],
                ["SHIFT", "~~", "Z", "X", "C", "V", "B", "N", "M", "<", ">","?", "     SHIFT"],
                ["fn", "ctrl", "\ =", "cmd", " ", "cmd", "\ =", "<<", "--", "   ^^", ">>"]]
        self.openingAppleLogo = AppleLogo(20, (self.topLeft[0] + self.topRight[0]) / 2, 200, "black","white") # Apple Logo while opening 
        self.openingProgressBar = ProgressBar(10, (self.topLeft[0] + self.topRight[0]) / 2 + 105, 70.5, 200, 6, "grey", "black") # Progress Bar while opening
        self.wallpaper = Image(".//Images//screen1.gif", 0, 0)
        generalDrawing.__init__(self, self.t)
        

    def drawQuadrilateral(self, topLeft, topRight, bottomRight, bottomLeft, curve=0, lineColor=None, colorFill=None):
        return super().drawQuadrilateral(topLeft, topRight, bottomRight, bottomLeft, curve=curve, lineColor=lineColor, colorFill=colorFill)
    
    def gotoInv(self, turtleCursor, x, y):
        return super().gotoInv(turtleCursor, x, y)
    
    def setTracerFast(self):
        self.scr.tracer(0)

    def draw(self):
        self.drawScreen()
        self.drawKeyBoard()
        self.drawPad()
        self.drawPowBut()

        # self.drawQuadrilateral((-194, -27), (182, -22), (187, -22), (-190, -27), 5, (22,26,31))
        # self.drawQuadrilateral((-240, -5), (240, -5), (240, -21), (-240, -21), 0, "black")

        self.t.color([125] * 3)
        self.gotoInv(self.t, (self.bottomLeft[0] +  self.bottomRight[0]) / 2, self.bottomRight[1] + 10 )
        self.t.write("MacBook Pro", False, 'center', ("Arial", 9))
        self.drawKeys()
    
    def clear(self):
        self.openingProgressBar.clear()
        self.openingAppleLogo.clear()
        self.t.clear()

    def drawPowBut(self):
        self.scr.tracer(True)
        powerButton = Image(".//Images//power.gif", self.bottomRight[0] - 20, self.bottomRight[1] - 20)
        powerButton.draw()
        self.scr.tracer(False)
        
    def drawDesktop(self):
        self.wallpaper.draw()
        self.wallpaper.scr.mainloop()

    def drawScreen(self, screenColor=(6, 6, 8)):
        self.screenColor = screenColor
        self.drawQuadrilateral(self.topLeft, self.topRight, self.bottomRight, self.bottomLeft, 5, self.colorMap["lightGrey"])

        self.t.pensize(3)
        self.drawQuadrilateral(*self.pcScreenDimension, 5, "black", self.screenColor)

    def drawKeyBoard(self):
        self.y_diff = self.bottomLeft[1] - self.topLeft[1]
        
        self.keyboardTopLeft = (self.topLeft[0] + 25, self.topLeft[1] + self.y_diff - 2)
        self.keyboardTopRight = (self.topRight[0] - 28, self.topRight[1] + self.y_diff - 2)
        self.keyboardBottomRight = (self.bottomRight[0] + 40 , -2 * self.bottomRight[1] + self.y_diff + 30)
        self.keyboardBottomLeft = (self.bottomLeft[0] - 40,  -2 * self.bottomLeft[1] + self.y_diff + 15)

        self.drawQuadrilateral(self.keyboardTopLeft, self.keyboardTopRight, (self.keyboardBottomRight[0]+2, self.keyboardBottomRight[1]-10), (self.keyboardBottomLeft[0]-2, self.keyboardBottomLeft[1]-10), 5, (218,217,222))
        self.drawQuadrilateral(self.keyboardTopLeft, self.keyboardTopRight, self.keyboardBottomRight, self.keyboardBottomLeft, 5, (194,195,197))

    def drawPad(self):
        self.t.pensize(1)
        prevHeading = self.t.heading()
        self.touchPadWidth = (150 ) // self.scale
        self.touchPadHeight = (75) // self.scale
        bottomWidthMid = (self.bottomLeft[0] + self.bottomRight[0]) // 2
        self.touchPadPos = []
        self.gapUnderTouchpad = 10
        touchPadCurve = 10
        self.touchPadPos.append((bottomWidthMid - (self.touchPadWidth / 2) - touchPadCurve, self.keyboardBottomLeft[1] + self.touchPadHeight + self.gapUnderTouchpad))
        self.touchPadPos.append((bottomWidthMid + (self.touchPadWidth / 2) , self.keyboardBottomLeft[1] + self.touchPadHeight + self.gapUnderTouchpad + touchPadCurve))
        self.touchPadPos.append((bottomWidthMid + (self.touchPadWidth / 2) + touchPadCurve, self.keyboardBottomLeft[1] + self.gapUnderTouchpad + touchPadCurve))
        self.touchPadPos.append((bottomWidthMid - (self.touchPadWidth / 2) , self.keyboardBottomLeft[1] + self.gapUnderTouchpad))
        print(self.touchPadPos)
        self.drawQuadrilateral(*self.touchPadPos, touchPadCurve,  (154,155,157), (201,202,204))
        self.t.setheading(prevHeading)


    def drawKeys(self):
        keyStartPos = [self.keyboardTopLeft[0] + 40, self.keyboardTopLeft[1] - 30]
        
        for i in range(len(self.letters)):
            extraSpace = 0
            for j in range(len(self.letters[i])):
                keyWidth = 29
                keyHeight =  20
                horizontalSpacing = 5
                verticalSpacing = 8
                keyCurve = 2
                bendConst = 0.3
                singleKey = self.letters[i][j]
                keyPos = (keyStartPos[0] + j * keyWidth - (i * 3) + extraSpace, keyStartPos[1] - i * keyHeight)
                if i == 0:
                    keyHeight -= 2
                    keyWidth += 1
                if i == 1 and j == 13:
                    keyWidth += 6
                if i == 2:
                    if j == 0:
                        keyWidth += 5
                        extraSpace += 5
                    elif j == 13:
                        keyWidth += 6
                if i == 3:
                    if j == 0:
                        keyWidth += 14
                        extraSpace += 14
                    elif j == 12:
                        extraSpace += 9
                    elif j == 13:
                        keyWidth -= 7
                        keyHeight += 10
                if i == 4:
                    if j == 0:
                        keyWidth += 3
                        extraSpace += 3 
                    elif j == 12:
                        keyWidth += 50
                if i == 5:
                    if j == 4:
                        keyWidth += 120
                        extraSpace += 120 
                    # elif j > 7:
                    #     keyWidth -= 5
                    #     horizontalSpacing -= 5
                    #     keyHeight -= 4            
                # print(keyPos, (keyPos[0] + keyWidth - horizontalSpacing, keyPos[1]), (keyPos[0] + keyWidth - horizontalSpacing, keyPos[1] + keyHeight - verticalSpacing), (keyPos[0] , keyPos[1] + keyHeight - verticalSpacing))
                self.drawQuadrilateral((keyPos[0],  keyPos[1] + keyHeight - verticalSpacing), (keyPos[0] + keyWidth - horizontalSpacing ,  keyPos[1] + keyHeight - verticalSpacing + keyCurve), (keyPos[0] + keyWidth - horizontalSpacing + (j *  bendConst), keyPos[1] + keyCurve), (keyPos[0] + (j * bendConst) , keyPos[1]), keyCurve, (12,13,17))
                self.t.color("white")
                self.gotoInv(self.t, keyPos[0] + 15, keyPos[1])
                self.t.write(singleKey, False, 'center', ("Arial", 6))

if __name__ == "__main__":
    isPCOpen = False
    isPCLoading = False
    pcPosition = [(-265, 295), (260, 300), (240, -15), (-235, -20)]
    # pcPosition = [(0, 295), (525, 300), (505, -15), (30, -20)]
    pcTopXCenter = (pcPosition[0][0] + pcPosition[1][0])//2
    pcBottomXCenter = (pcPosition[3][0] + pcPosition[2][0])//2
    pcTopYCenter = (pcPosition[0][1] + pcPosition[1][1]) // 2
    pcBack = PC_BACK(*pcPosition)
    pcFront = PC(1, *pcPosition)


    def next1(x, y):
        print("Click Position", x, y)
        global isPCOpen
        global isPCLoading
        if not isPCLoading:
            print(pcBack.topRight)
            if x in range(pcTopXCenter-50, pcTopXCenter+50) and y in range(pcTopYCenter-15, pcTopYCenter+15) and isPCOpen:
                pcFront.clear()
                pcBack.draw()
                isPCOpen = False
            elif x in range(pcBottomXCenter-50, pcBottomXCenter+50) and y in range(pcBack.bottomLeft[1]-15,pcBack.bottomLeft[1]) and not isPCOpen:
                pcBack.clear()
                pcFront.draw()
                isPCOpen = True
            elif x in range(pcBack.topRight[0]-12, pcBack.topRight[0]+2) and y in range(pcBack.topRight[1] - 20, pcBack.topRight[1] - 3) and isPCOpen and not isPCLoading:
                isPCLoading = True
                pcFront.drawScreen("white")
                pcFront.openingAppleLogo.draw()
                pcFront.openingProgressBar.draw()
                isPCLoading = False

    pcBack.draw()
    turtle.Screen().onclick(next1)
    pcFront.scr.mainloop()
