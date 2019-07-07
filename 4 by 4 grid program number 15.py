#Duvall Pinkney
#3/4/2015
#program number 15

from turtle import *

def main():
    #initialize ninja turtle
    win = Screen()
    ninja = Turtle()
    ninja.shape('turtle')

    # draw grid-------
    # 50 pixels x 50 pixels box with center at (x -25,y-25) pixels
    #
    ninja.down()
    ninja.forward(200)
    ninja.left(90)
    ninja.forward(200)
    ninja.left(90)
    ninja.forward(200)
    ninja.left(90)
    ninja.forward(200)
    # at point (0,0)
    ninja.left(90)
    ninja.forward(50)
    ninja.left(90)
    ninja.forward(200)
    #point (50,200)
    ninja.right(90)
    ninja.forward(50)
    ninja.right(90)
    ninja.forward(200)
    #point (100,0)
    ninja.left(90)
    ninja.forward(50)
    ninja.left(90)
    ninja.forward(200)
    #point (150,200)
    ninja.right(90)
    ninja.forward(50)
    ninja.right(90)
    ninja.forward(50)
    ninja.right(90)
    ninja.forward(200)
    #point (0 ,150)
    ninja.left(90)
    ninja.forward(50)
    ninja.left(90)
    ninja.forward(200)
    #point(200,50)
    ninja.right(90)
    ninja.forward(50)
    ninja.right(90)
    ninja.forward(200)
    ninja.left(90)
    ninja.forward(50)
    ninja.left(90)
    ninja.up()
    #at point (0,0)
    #--------------------end grid construction--------------------------------------
    #get user input
    x,y = eval(input("Please enter coordinates: "))
    neoX = x * 50 - 25
    neoY = y * 50 - 25
    
    ninja.goto(neoX,neoY)
    ninja.write("2")
    print("Please hit the enter key to continue: ")
    ninja.left(180)
    if neoX >= 100:
        neoX = neoX - 100
        ninja.goto(neoX,neoY)
        ninja.write("2")
        ninja.goto(0,0)
    else:
        neoX = neoX - 50
        ninja.goto(neoX,neoY)
        ninja.write("2")
        ninja.goto(0,0)


main()
