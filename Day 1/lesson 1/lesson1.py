from turtle import *

#we want to paint a house

#step 1: draw a square

speed(7)
width(7)
color("purple")
forward(300)
left(90)
forward(200)
left(90)
forward(300)
left(90)
forward(200)
left(90)
#end of square


#step 2: drawing a door


forward(115)
color("yellow")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()



penup()
goto(300,200)
pendown()

# drawing a roof

color("red")
begin_fill()
right(135)
forward(210)
left(90)
forward(210)
end_fill()

#drawing windows

width(5)
color("purple")
left(45)
forward(75)

color("white")
left(90)
forward(20)

color("green")
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

color("white")
forward(125)

color("purple")
left(90)
forward(260)

color("white")
left(90)
forward(125)

color("green")
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()


exitonclick()