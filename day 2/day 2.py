from turtle import *


# i want to make a house

#step 1:  draw a square


width (10)

color ('red')

forward(200)
left(90)

forward(200)
left(90)

forward(200)    
left(90)

forward(200)
left(90)
#end of aquare 

#drawing a door



forward(70)
color('orange')
begin_fill()
left(90)
forward(120)      #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color ('yellow')      
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


color('white')
penup()
goto(150,151)
color("cyan")  
begin_fill()                      #making windows
left(30)
forward(50)
left(90)
forward(25)
left(90)
forward(50)
left(25)
end_fill()



color('white')
penup()
goto(50,151)
color('cyan')
begin_fill()   #making windows
left(155)
forward(50)
right(90)
forward(25)
right(90)
forward(50)
right(25)
end_fill()

                  




#house done





color("white")
penup()
goto(-500,-10)
color("green")
begin_fill()
right(65)
forward(1000)
right(90)
forward(500)
right(90)
forward(1000)
end_fill()

penup()
goto(500,-10)
color("white")
goto(-400,300)
color("yellow")
begin_fill()
circle(50)
end_fill()


color("white")
penup()
goto(-300,0)
color("brown")
begin_fill()
right(90)
forward(150)
right(90)
forward(50)
right(90)
forward(150)
end_fill()


begin_fill()
penup()
goto(-330,150)
color("green")
circle(55)
end_fill()



goto(300,0)
right(90)
color("brown")
begin_fill()
right(90)
forward(150)
right(90)
forward(50)
right(90)
forward(150)
end_fill()


left(180)
forward(200)
left(90)
forward(25)
begin_fill()
penup()
color("green")
circle(55)
end_fill()





exitonclick()