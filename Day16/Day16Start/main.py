import turtle
import another_module
print(another_module.another_variable)
from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")

my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)
timmy.forward(100)
timmy.left(45)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
my_screen.exitonclick()