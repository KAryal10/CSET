'''Use turtle graphics and Python to create a graphical landscape. 

1) The bottom half of the screen should be green.

2) The top half of the screen should be blue.

3) Draw grey mountains in the background using triangles.  Create at least 3 mountains of varying sizes.

4) Draw an orange truck with black tires in the foreground.

5) Draw your initials in the bottom right corner.

6) Include these instructions as comments at the beginning of your program.  Also comment each section, i.e. draw mountain, draw truck, etc.

Attach your .py file to Blackboard.  Make sure you attach your .py file and not the .pyproj file.  If you attach the wrong file you will get zero credit.

Don't forget the instructions as comments as well as code comments or you will loose points.'''

import turtle #importing turtle graphics library

# setting up our turtle by hiding it and setting speed to 0 and screen size to 700*650
turtle.hideturtle()
turtle.speed(0)
turtle.setup(700,650)

#setting background color as blue which represents sky
turtle.bgcolor("blue")

#starting to fill bottom half of the screen to green drawing a rectangular fill 
turtle.fillcolor("green") 
turtle.begin_fill() 
turtle.forward(350)
turtle.right(90)
turtle.forward(325)
turtle.right(90)
turtle.forward(700)
turtle.right(90)
turtle.forward(325)
turtle.right(90)
turtle.forward(350)
turtle.end_fill()

#going to (-335,0) to draw a grey mountain of first size
turtle.goto(-335,0)
turtle.fillcolor("grey")
turtle.begin_fill()
for a in range(3):
    turtle.forward(200)
    turtle.left(120)
turtle.end_fill()

#going to (-135,0) to draw a grey mountain of second size
turtle.goto(-135,0)
turtle.begin_fill()
for a in range(3):
    turtle.forward(300)
    turtle.left(120)
turtle.end_fill()

#going to (165,0) to draw a grey mountain of third size
turtle.goto(165,0)
turtle.begin_fill()
for n in range(3):
    turtle.forward(170)
    turtle.left(120)
turtle.end_fill()

# going to (165,12.5) to draw the body of an orange truck 
turtle.penup()
turtle.goto(165,12.5)
turtle.pendown()
turtle.right(180)
turtle.fillcolor("orange")
turtle.begin_fill()
turtle.forward(175)
turtle.right(90)
turtle.forward(35)
turtle.right(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(35)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(35)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(35)
turtle.end_fill()
turtle.right(90)

# going to (125,25) to draw a black back tyre of the truck
turtle.penup()
turtle.goto(125,25)
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(12.5)
turtle.end_fill()

# going to (25,25) to draw a black front tyre of the truck
turtle.penup()
turtle.goto(25,25)
turtle.pendown()
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(12.5)
turtle.end_fill()
turtle.right(90)

# drwaing a window for the truck and filling it with white color
turtle.penup()
turtle.goto(25,42.5)
turtle.pendown()
turtle.fillcolor("white")
turtle.begin_fill()
for n in range(4):
    turtle.forward(30)
    turtle.right(90)
turtle.end_fill()

#drawing my first initial 'K' at the bottom right corner of the screen
turtle.penup()
turtle.goto(275,-300)
turtle.pendown()
turtle.forward(16)
turtle.right(180)
turtle.forward(8)
turtle.left(120)
turtle.forward(10)
turtle.right(180)
turtle.forward(10)
turtle.left(120)
turtle.forward(10)

#drawing my second initial 'A' next to my first initial
turtle.penup()
turtle.goto(285,-300)
turtle.pendown()
turtle.left(120)
turtle.goto(290,-284)
turtle.right(120)
turtle.goto(295,-300)
turtle.right(215)
turtle.forward(8)
turtle.left(60)
turtle.forward(6)

#setting turtle to only exit when clicked 
turtle.exitonclick()