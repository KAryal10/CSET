'''Python Programming Assignment: Creative Shapes with Turtle Graphics
Objective:
This assignment is designed to help you practice your Python programming skills, focusing on the use of functions, loops, and the Turtle graphics library. You will create a program that draws various shapes with customizable attributes, enhancing your understanding of graphical programming and function definitions in Python.
Assignment Description:
Write a Python program that utilizes Turtle graphics to draw a series of shapes based on user-defined functions. The shapes to be drawn include a circle, an square, a star (5-point), and a hexagon. Each shape should be drawn at a specified X and Y location, with customizable size, pen color, and orientation angle.
For the star, you will need to think creatively about how to use Turtle graphics to achieve the desired appearance, as these shapes are not directly supported by Turtle's standard functions.
Function Parameters:
Each function should accept parameters for X, Y (default value of 0 for both), size/radius (default value of 100), angle (default value of 0), and color (default value of "black"). 
Requirements:
Use loops within your shape-drawing functions to minimize repetition in your code.
Incorporate Python's Turtle graphics library to execute the drawing commands.
Ensure your program includes calls to each shape-drawing function with various sizes, colors, and orientation angles to demonstrate their versatility. Do not ask for user input; instead, hard-code the values for these parameters within your script.
You will need to use the turtle methods setheading and goto for each shape.
Include a detailed comment header in your script with the problem description, and comment your code thoroughly to explain your logic and the purpose of each function and parameter.
Extra Credit:
Implement an additional function called customshape that draws any shape based on a list of points (list of X and Y coordinates) provided as a parameter. This function should demonstrate the ability to draw complex, custom shapes beyond the predefined ones. Include a sample call for this function as well.'''

import turtle #importing turtle graphics library

# setting up our turtle by hiding it and setting speed to 0 and screen size to 700*650
turtle.hideturtle()
turtle.speed(0)
turtle.setup(1000,750)

#function to create a circle with the specified parameters
#Parameters include starting points, radius, angle to start with, and color
#Start with setting angle and then goto starting point without drawing any line and then drawing circle of specified radius with the fill color
def drawCircle(X=0, Y=0, radius=100, angle=0, color="black"):
    turtle.setheading(angle)
    turtle.penup()
    turtle.goto(X,Y)
    turtle.pendown()
    turtle.fillcolor(color) 
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

#function to create a square with the specified parameters
#Parameters include starting points, size of each line, angle to start with, and color
#Start with setting angle and then goto starting point without drawing any line then move forward according to the size and turning right by 90 degrees and repeating it three more times
def drawSquare(X=0, Y=0, size=100, angle=0, color="black"):
    turtle.setheading(angle)
    turtle.penup()
    turtle.goto(X,Y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

#function to create a star with the specified parameters
#Parameters include starting points, size of each line, angle to start with, and color
#Start with setting angle and then goto starting point without drawing any line then move forward according to the size and turning right by 36 degrees. Again move forward according to the size and turn left by 108 degrees. This completes one arm of the star and repeat it four more times
def drawStar(X=0, Y=0, size=100, angle=0, color="black"):
    turtle.setheading(angle)
    turtle.penup()
    turtle.goto(X,Y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(size)
        turtle.right(36)
        turtle.forward(size)
        turtle.left(108)    
    turtle.end_fill()

#function to create a hexagon with the specified parameters
#Parameters include starting points, size of each line, angle to start with, and color
#Start with setting angle and then goto starting point without drawing any line then move forward according to the size and turn right by 60 degrees. Repeat it five more times
def drawHexagon(X=0, Y=0, size=100, angle=0, color="black"):
    turtle.setheading(angle)
    turtle.penup()
    turtle.goto(X,Y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(6):
        turtle.forward(size)
        turtle.right(60)
    turtle.end_fill()

#function to create a custom Shape with the specified parameters
#Parameters include list of points where the lines are connected and color. List have the list of points where the points are list of x and y coordinates
#get the first points in list and draw the line to the second point and repeat it until we reach the end of the list
def drawCustomShape(list=[[0,0],[100,100],[300,100],[300,50]],color="black"):
    turtle.penup()
    turtle.goto(list[0][0],list[0][1])
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in list:
        turtle.goto(i)
    turtle.goto(list[0][0],list[0][1])
    turtle.end_fill()

#calling each function to create shape 
drawCustomShape([[0,0],[0,200],[300,300],[300,200],[100,-50]],"red")
drawCircle(-100,-10,50,10,"blue")
drawSquare(50,-100,200,30,"yellow")
drawStar(-200,150,60,20,"green")
drawHexagon(-200,-200,75,50)

turtle.exitonclick()