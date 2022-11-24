import turtle as turtle_mode
from main import color_list
import random

turtle_mode.colormode(255)
t = turtle_mode.Turtle()




def form():
    t.dot(20)
    t.penup()
    t.fd(50)
    t.pendown()




t.speed("fastest")


t.penup()
t.setpos(0,-200)
y = -150
for _ in range(10):

    for _ in range(10):
        t.color(random.choice(color_list))
        form()
    t.penup()
    t.setpos(0, y)
    y += 50

screen = turtle_mode.Screen()
screen.exitonclick()
