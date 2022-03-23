#Printing Wistron Name using Python Turtle

import turtle  #Importing Turtle
g = turtle.Turtle() #Naming turtle as "g"
g.speed(200) #Speed of the pen
g.hideturtle()           #make the turtle invisible

#Positioning the Turtle point before start writing the letters
g.penup() #don't draw when turtle moves
g.right(180)
g.forward(400)
g.left(180)
g.pendown() #draw when the turtle moves

#Priniting letter "W"

g.color('black', '#016795')
g.begin_fill()
g.forward(30)
g.right(75)
g.forward(100)
g.left(150)
g.forward(100)
g.right(75)
g.forward(45)
g.right(75)
g.forward(100)
g.left(150)
g.forward(100)
g.right(75)
g.forward(30)
g.right(105)
g.forward(130)
g.right(75)
g.forward(45)
g.right(75)
g.forward(100)
g.left(150)
g.forward(100)
g.right(75)
g.forward(45)
g.right(75)
g.forward(130)
g.end_fill()

#Positioning pen for printing "I"
g.penup()
g.right(105)
g.forward(219)
g.pendown()

#Printing letter "I"
g.color("black","#A2CC57")
g.begin_fill()
g.right(90)
g.forward(125)
g.left(90)
g.forward(30)
g.left(90)
g.forward(125)
g.left(90)
g.end_fill()
g.color("black","#016795")
g.begin_fill()
g.forward(30)
g.right(90)
g.forward(30)
g.right(90)
g.forward(30)
g.right(90)
g.forward(30)
g.end_fill()

##Positioning pen for printing "S"
g.left(90)
g.penup()
g.forward(50)
g.circle(-35,-185)
g.pendown()

# Printing letter "S"
g.color('black', '#016795')
g.begin_fill()
g.circle(20,-250)
g.right(90)
g.forward(30)
g.left(90)
g.circle(50,220)
g.right(300)
g.circle(-16.5,270)
g.left(90)
g.forward(30)
g.left(90)
g.circle(44.5,215)
g.end_fill()

#Positioning pen for printing "T"

g.penup()
g.left(110)
g.forward(102)
g.right(90)
g.forward(87)
g.pendown()

#Printing letter "T"

g.color("black","#016795")
g.begin_fill()
g.right(90)
g.forward(30)
g.right(90)
g.forward(30)
g.left(90)
g.forward(30)
g.left(90)
g.forward(30)
g.right(90)
g.forward(70)
g.circle(40,100)
g.left(80)
g.forward(25)
g.right(90)
g.circle(20,-90)
g.right(180)
g.forward(64)
g.right(90)
g.forward(40)
g.left(90)
g.forward(30)
g.left(90)
g.forward(40)
g.right(90)
g.forward(30)
g.left(90)
g.forward(30)
g.end_fill()

##Positioning pen for printing "R"

g.penup()
g.right(180)
g.forward(80)
g.right(90)
g.forward(30)
g.pendown()

#Printing letter "R"
g.color("black","#016795")
g.begin_fill()
g.forward(135)
g.left(90)
g.forward(30)
g.left(90)
g.forward(80)
g.circle(-30,130)
g.left(130)
g.forward(30)
g.left(45)
g.circle(30,130)
g.left(185)
g.forward(20)
g.left(90)
g.forward(30)
g.end_fill()


##Positioning pen for printing "O"

g.penup()
g.left(180)
g.forward(70)
g.right(90)
g.forward(70)
g.pendown()

#Printing Letter "R"
g.color("black","#016795")
g.begin_fill()
g.circle(65,-360,300)
g.penup()
g.left(90)
g.forward(30)
g.left(270)
g.pendown()
g.circle(32.5,360,300)
g.end_fill()

#Positioning pen for printing "N"


g.penup()
g.left(90)
g.forward(110)
g.left(90)
g.forward(71)
g.right(180)
g.forward(15)
g.pendown()

#Printing letter "N"
g.color("black","#016795")
g.begin_fill()
g.forward(120)
g.left(90)
g.forward(30)
g.left(90)
g.forward(80)
g.circle(-20,180,300)
g.forward(80)
g.left(90)
g.forward(30)
g.left(90)
g.forward(80)
g.circle(40,140,300)
g.right(140)
g.forward(15)
g.left(90)
g.forward(31)
g.end_fill()
turtle.exitonclick()
