#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(anicet, sides):
    for s in range(sides):
        anicet.forward(60)
        anicet.right(360/sides)
        
def fillCorner(tfue, corner):
    #draw big square
    drawSquare(tfue, 100)
    
    if corner ==1:
         
        tfue.begin_fill()
        drawSquare(tfue, 50)
        tfue.end_fill()
         
    elif corner ==2:
        tfue.forward(50)
        tfue.begin_fill()
        drawSquare(tfue, 50)
        tfue.end_fill()
         
    elif corner ==3:
        tfue.right(-270)
        tfue.forward(50)
        tfue.left(90)
        tfue.begin_fill()
        drawSquare(tfue, 50)
        tfue.end_fill()
        
    elif corner ==4:
        tfue.forward(100)
        tfue.right(90)
        tfue.forward(50)
        tfue.begin_fill()
        drawSquare(tfue, 50)
        tfue.end_fill()
        
def squaresInSquares(mouse, num):
    drawSquare(mouse, 190)
    
    if num == 1:
        mouse.pendown()
        mouse.goto(-5,-5)
        mouse.forward(10)
        drawSquare(mouse, 180)
    elif num ==2:
        mouse.pendown()
        mouse.goto(-5,-5)
        mouse.forward(10)
        drawSquare(mouse, 180)
        mouse.pendown()
        mouse.goto(-10,-10)
        mouse.forward(20)
        drawSquare(mouse, 170)
    elif num ==3:
        mouse.pendown()
        mouse.goto(-5,-5)
        mouse.forward(10)
        drawSquare(mouse, 180)
        mouse.pendown()
        mouse.goto(-10,-10)
        mouse.forward(20)
        drawSquare(mouse, 170)
        mouse.pendown()
        mouse.goto(-15,-15)
        mouse.forward(30)
        drawSquare(mouse, 160)
    elif num ==4:
        mouse.pendown()
        mouse.goto(-5,-5)
        mouse.forward(10)
        drawSquare(mouse, 180)
        mouse.pendown()
        mouse.goto(-10,-10)
        mouse.forward(20)
        drawSquare(mouse, 170)
        mouse.pendown()
        mouse.goto(-15,-15)
        mouse.forward(30)
        drawSquare(mouse, 160)
        mouse.pendown()
        mouse.goto(-20,-20)
        mouse.forward(40)
        drawSquare(mouse, 150)
    elif num ==5:
        mouse.pendown()
        mouse.goto(-5,-5)
        mouse.forward(10)
        drawSquare(mouse, 180)
        mouse.pendown()
        mouse.goto(-10,-10)
        mouse.forward(20)
        drawSquare(mouse, 170)
        mouse.pendown()
        mouse.goto(-15,-15)
        mouse.forward(30)
        drawSquare(mouse, 160)
        mouse.pendown()
        mouse.goto(-20,-20)
        mouse.forward(40)
        drawSquare(mouse, 150)
        mouse.pendown()
        mouse.goto(-25,-25)
        mouse.forward(50)
        drawSquare(mouse, 140)
    elif num ==6:
        mouse.pendown()
        mouse.goto(-5,-5)
        mouse.forward(10)
        drawSquare(mouse, 180)
        mouse.pendown()
        mouse.goto(-10,-10)
        mouse.forward(20)
        drawSquare(mouse, 170)
        mouse.pendown()
        mouse.goto(-15,-15)
        mouse.forward(30)
        drawSquare(mouse, 160)
        mouse.pendown()
        mouse.goto(-20,-20)
        mouse.forward(40)
        drawSquare(mouse, 150)
        mouse.pendown()
        mouse.goto(-25,-25)
        mouse.forward(50)
        drawSquare(mouse, 140)
        mouse.pendown()
        mouse.goto(-30,-30)
        mouse.forward(60)
        drawSquare(mouse, 130)
    elif num ==7:
        mouse.pendown()
        mouse.goto(-5,-5)
        mouse.forward(10)
        drawSquare(mouse, 180)
        mouse.pendown()
        mouse.goto(-10,-10)
        mouse.forward(20)
        drawSquare(mouse, 170)
        mouse.pendown()
        mouse.goto(-15,-15)
        mouse.forward(30)
        drawSquare(mouse, 160)
        mouse.pendown()
        mouse.goto(-20,-20)
        mouse.forward(40)
        drawSquare(mouse, 150)
        mouse.pendown()
        mouse.goto(-25,-25)
        mouse.forward(50)
        drawSquare(mouse, 140)
        mouse.pendown()
        mouse.goto(-30,-30)
        mouse.forward(60)
        drawSquare(mouse, 130)
        mouse.pendown()
        mouse.goto(-35,-35)
        mouse.forward(70)
        drawSquare(mouse, 120)
    elif num ==8:
        mouse.pendown()
        mouse.goto(-5,-5)
        mouse.forward(10)
        drawSquare(mouse, 180)
        mouse.pendown()
        mouse.goto(-10,-10)
        mouse.forward(20)
        drawSquare(mouse, 170)
        mouse.pendown()
        mouse.goto(-15,-15)
        mouse.forward(30)
        drawSquare(mouse, 160)
        mouse.pendown()
        mouse.goto(-20,-20)
        mouse.forward(40)
        drawSquare(mouse, 150)
        mouse.pendown()
        mouse.goto(-25,-25)
        mouse.forward(50)
        drawSquare(mouse, 140)
        mouse.pendown()
        mouse.goto(-30,-30)
        mouse.forward(60)
        drawSquare(mouse, 130)
        mouse.pendown()
        mouse.goto(-35,-35)
        mouse.forward(70)
        drawSquare(mouse, 120)
        mouse.pendown()
        mouse.goto(-40,-40)
        mouse.forward(80)
        drawSquare(mouse, 110)
    elif num ==9:
        mouse.pendown()
        mouse.goto(-5,-5)
        mouse.forward(10)
        drawSquare(mouse, 180)
        mouse.pendown()
        mouse.goto(-10,-10)
        mouse.forward(20)
        drawSquare(mouse, 170)
        mouse.pendown()
        mouse.goto(-15,-15)
        mouse.forward(30)
        drawSquare(mouse, 160)
        mouse.pendown()
        mouse.goto(-20,-20)
        mouse.forward(40)
        drawSquare(mouse, 150)
        mouse.pendown()
        mouse.goto(-25,-25)
        mouse.forward(50)
        drawSquare(mouse, 140)
        mouse.pendown()
        mouse.goto(-30,-30)
        mouse.forward(60)
        drawSquare(mouse, 130)
        mouse.pendown()
        mouse.goto(-35,-35)
        mouse.forward(70)
        drawSquare(mouse, 120)
        mouse.pendown()
        mouse.goto(-40,-40)
        mouse.forward(60)
        drawSquare(mouse, 120)
        mouse.pendown()
        mouse.goto(-45,-45)
        mouse.forward(80)
        drawSquare(mouse, 110)
    elif num ==9:
        mouse.pendown()
        mouse.goto(-5,-5)
        mouse.forward(10)
        drawSquare(mouse, 180)
        mouse.pendown()
        mouse.goto(-10,-10)
        mouse.forward(20)
        drawSquare(mouse, 170)
        mouse.pendown()
        mouse.goto(-15,-15)
        mouse.forward(30)
        drawSquare(mouse, 160)
        mouse.pendown()
        mouse.goto(-20,-20)
        mouse.forward(40)
        drawSquare(mouse, 150)
        mouse.pendown()
        mouse.goto(-25,-25)
        mouse.forward(50)
        drawSquare(mouse, 140)
        mouse.pendown()
        mouse.goto(-30,-30)
        mouse.forward(60)
        drawSquare(mouse, 130)
        mouse.pendown()
        mouse.goto(-35,-35)
        mouse.forward(70)
        drawSquare(mouse, 120)
        mouse.pendown()
        mouse.goto(-40,-40)
        mouse.forward(80)
        drawSquare(mouse, 110)
        mouse.pendown()
        mouse.goto(-45,-45)
        mouse.forward(90)
        drawSquare(mouse, 100)
        mouse.pendown()
        mouse.goto(-50,-50)
        mouse.forward(100)
        drawSquare(mouse, 90)
    elif num ==10:
        mouse.pendown()
        mouse.goto(-5,-5)
        mouse.forward(10)
        drawSquare(mouse, 180)
        mouse.pendown()
        mouse.goto(-10,-10)
        mouse.forward(20)
        drawSquare(mouse, 170)
        mouse.pendown()
        mouse.goto(-15,-15)
        mouse.forward(30)
        drawSquare(mouse, 160)
        mouse.pendown()
        mouse.goto(-20,-20)
        mouse.forward(40)
        drawSquare(mouse, 150)
        mouse.pendown()
        mouse.goto(-25,-25)
        mouse.forward(50)
        drawSquare(mouse, 140)
        mouse.pendown()
        mouse.goto(-30,-30)
        mouse.forward(60)
        drawSquare(mouse, 130)
        mouse.pendown()
        mouse.goto(-35,-35)
        mouse.forward(70)
        drawSquare(mouse, 120)
        mouse.pendown()
        mouse.goto(-40,-40)
        mouse.forward(80)
        drawSquare(mouse, 110)
        mouse.pendown()
        mouse.goto(-45,-45)
        mouse.forward(90)
        drawSquare(mouse, 100)
        mouse.pendown()
        mouse.goto(-50,-50)
        mouse.forward(100)
        drawSquare(mouse, 90)
        mouse.pendown()
        mouse.goto(-55,-55)
        mouse.forward(110)
        drawSquare(mouse, 80)
        

        
        
        
        
        
        




    
    
def main():
    myTurtle = turtle.Turtle()
    
    #drawSquare(myTurtle, 100)
    
    
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
