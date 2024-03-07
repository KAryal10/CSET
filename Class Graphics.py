'''Python Programming Assignment: Class-Based Graphics with Turtle

Objective:
This assignment is designed to enhance your understanding of class-based programming in Python, focusing on the implementation of encapsulation and method definitions. Using the Turtle graphics library, you will create classes to draw various geometric shapes, each with customizable attributes. This approach will help you appreciate the benefits of organizing code into modular, reusable components.

Assignment Description:
Develop a Python program that employs the Turtle graphics library to draw a collection of shapes, including a circle, a square, a star (5-point), and a hexagon. Each shape will be represented by its own class, with each class containing methods to initialize the shape's properties and to draw the shape on the screen. These properties include the shape's position (X, Y coordinates), size, pen color, and orientation angle.  Your code should be based on your code from the previous function assignment. 

Shape Specifications:

Separate Classes: Implement a separate class for each shape: Circle, Square, Star, and Hexagon. 
Common Methods: Each class should include an __init__ method to initialize the shape's attributes and a draw method to define how the shape is drawn using Turtle graphics.
Set & Get Methods:

Create a set and get method for the size or radius attribute for each class and include example method calls for each.
Class Attributes:

Attributes for each class should include X and Y coordinates (defaulting to 0), size/radius (defaulting to 100), orientation angle (defaulting to 0), and color (defaulting to "black").
Requirements:

Each shape class must encapsulate its own data and behavior, demonstrating the principle of encapsulation.
Avoid redundancy by using Turtle's drawing commands efficiently within each draw method.
Demonstrate that you can convert functions into classes and methods.
Instantiate objects of each shape class with various sizes, colors, and orientation angles to display their versatility. These parameters should be hardcoded in your script, with no user input required.
Ensure that each class has a method to position the shape using Turtle's setheading and goto methods before drawing.
Documentation:

Provide a comprehensive comment header in your script, detailing the assignment purpose, a description of each class, and the purpose of the __init__ and draw methods.
Comment your code to clarify the logic behind your shape drawing implementations and the use of class-based programming concepts.
Extra Credit:

The CustomShape class should accept a list of (X, Y) coordinates and draw a shape based on these points. This will challenge your ability to handle more complex, dynamic data structures within a class-based framework. 
Submission Instructions:

Attach your .py Python script file.
Include an image showcasing the shapes drawn in different colors and orientations as part of your submission.
Make sure your submission meets all the outlined requirements for full credit.'''

import turtle #importing turtle graphics library

# setting up our turtle by hiding it and setting speed to 0 and screen size to 1000*750
turtle.hideturtle()
turtle.speed(0)
turtle.setup(1000,750)

'''This is a circle class with the attributes X and Y for  starting position, radius of cicle, angle for the starting orientation and color for fill color.
The __init__ method is to initialize the circle object with the default starting position of 0,0, radius of 100, angle of 0 and black fill color.
The draw method here starts drawing by using startingpostion method to go to the starting position and draws the shape.
'''
class Circle:
    
    def __init__(self,X=0, Y=0, radius=100, angle=0, color="black"):
        self.X=X
        self.Y=Y
        self.radius=radius
        self.angle=angle
        self.color=color
    def setRadius(self,radius): 
        self.radius=radius
    def getRadius(self):
        return self.radius
    def startingPosition(self):
        turtle.penup()
        turtle.goto(self.X,self.Y)
        turtle.setheading(self.angle)

    # the draw method calls startingpostion method to go to the starting position without drawing and then use the pendown to start drawing
    #fillcolor sets the color and by using turtle.circle with the paratmeter radius it drraws the shape of circle of gicen radius
    def draw(self):    
        self.startingPosition()
        turtle.pendown()
        turtle.fillcolor(self.color) 
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.end_fill()

'''This is a Square class with the attributes X and Y for  starting position, size of a side, angle for the starting orientation and color for fill color.
The __init__ method is to initialize the square object with the default starting position of 0,0, size of 100, angle of 0 and black fill color.
The draw method here starts drawing by using startingpostion method to go to the starting position and draws the shape.
'''
class Square:
    def __init__(self,X=0, Y=0, size=100, angle=0, color="black"):
        self.X=X
        self.Y=Y
        self.size=size
        self.angle=angle
        self.color=color
    def setSize(self,size):
        self.size=size
    def getSize(self):
        return self.size
    def startingPosition(self):
        turtle.penup()
        turtle.goto(self.X,self.Y)
        turtle.setheading(self.angle)

    # the draw method calls startingpostion method to go to the starting position without drawing and then use the pendown to start drawing
    #fillcolor sets the color and by using turtle.forward with the paratmeter size it draws a line and using right(90) it turns right and repeat again 3 times to complete the square
    def draw(self):
        self.startingPosition()
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(self.size)
            turtle.right(90)
        turtle.end_fill()

'''This is a Star class with the attributes X and Y for  starting position, size of a side, angle for the starting orientation and color for fill color.
The __init__ method is to initialize the Star object with the default starting position of 0,0, size of 100, angle of 0 and black fill color.
The draw method here starts drawing by using startingpostion method to go to the starting position and draws the shape.
'''
class Star:
    def __init__(self,X=0, Y=0, size=100, angle=0, color="black"):
        self.X=X
        self.Y=Y
        self.size=size
        self.angle=angle
        self.color=color
    def setSize(self,size):
        self.size=size
    def getSize(self):
        return self.size
    def startingPosition(self):
        turtle.penup()
        turtle.goto(self.X,self.Y)
        turtle.setheading(self.angle)

    # the draw method calls startingpostion method to go to the starting position without drawing and then use the pendown to start drawing
    #fillcolor sets the color and by using turtle.forward with the paratmeter size followed by turning right by 36 degree, foward to the size and turning left by 108 degree creates one head of the star. now repeating it 4 times will create a complete 5 point star.
    def draw(self):
        self.startingPosition()
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(self.size)
            turtle.right(36)
            turtle.forward(self.size)
            turtle.left(108)    
        turtle.end_fill()

'''This is a Hexagon class with the attributes X and Y for  starting position, size of a side, angle for the starting orientation and color for fill color.
The __init__ method is to initialize the Hexagon object with the default starting position of 0,0, size of 100, angle of 0 and black fill color.
The draw method here starts drawing by using startingpostion method to go to the starting position and draws the shape.
'''
class Hexagon:
    def __init__(self,X=0, Y=0, size=100, angle=0, color="black"):
        self.X=X
        self.Y=Y
        self.size=size
        self.angle=angle
        self.color=color
    def setSize(self,size):
        self.size=size
    def getSize(self):
        return self.size
    def startingPosition(self):
        turtle.penup()
        turtle.goto(self.X,self.Y)
        turtle.setheading(self.angle)

    # the draw method calls startingpostion method to go to the starting position without drawing and then use the pendown to start drawing
    #fillcolor sets the color and by using turtle.forward with the paratmeter size followed by turning right by 60 degree creates one side of the hexagon. now repeating it 5 times will create a complete Hexagon
    def draw(self):
        self.startingPosition()
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        for i in range(6):
            turtle.forward(self.size)
            turtle.right(60)
        turtle.end_fill()

'''This is a customShape class with the attributes list for the points of shape and color for fill color.
The __init__ method is to initialize the customShape object with the default list values of (0,0), (100,100), (300,100), (300,50) and black fill color.
The draw method here starts drawing by using startingpostion method to go to the starting position and draws the shape.
'''
class customShape:
    def __init__(self,list=[[0,0],[100,100],[300,100],[300,50]],color="black"):
        self.list=list
        self.color=color
    def startingPosition(self):
        turtle.penup()
        turtle.goto(self.list[0][0],self.list[0][1])

    # the draw method calls startingpostion method to go to the starting position without drawing which is the first point of the list and then use the pendown to start drawing
    #fillcolor sets the color and by using turtle.goto the points of list using for loop connects all the line and again using the goto to go to the first points will connect all the line and creates a custom shape
    def draw(self):
        self.startingPosition()
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        for i in self.list:
            turtle.goto(i)
        turtle.goto(self.list[0][0],self.list[0][1])
        turtle.end_fill()


circle=Circle(X=-100,Y=-10,angle=10,color="blue")  #creating aand initializing a Circle object with the values of attributes as parameter
circle.setRadius(50)    #setting the radius of 50
print(circle.getRadius())   #printing the raius of circle
circle.draw()      #drawing the circle
sq=Square(X=50,Y=-100,angle=30,color="yellow") #creating aand initializing a square object with the values of attributes as parameter
sq.setSize(200) #setting the size of 200
print(sq.getSize()) #printing the size of square
sq.draw()   #drawing the square
st=Star(X=-200,Y=150,angle=20,color="green")    #creating aand initializing a star object with the values of attributes as parameter
st.setSize(60)  #setting the size of 60
print(st.getSize()) #printing the size of star
st.draw()   #drawing the star
he=Hexagon(X=-200,Y=-200,angle=50)   #creating aand initializing a hexagon object with the values of attributes as parameter
he.setSize(75)  #setting the size of 75
print(he.getSize()) #printing the size of hexagon
he.draw()   #drawing the hexagon

c=customShape([[0,0],[0,200],[300,300],[300,200],[100,-50]],"red") #creating aand initializing a customShape object with the values of attributes as parameter
c.draw()    #drawing the custom shape

turtle.exitonclick()
