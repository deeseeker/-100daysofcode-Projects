from turtle import Turtle, Screen
import random
t = Turtle()

# parallel lines
# for i in range(15):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()

# drawing different shapes
n = 3
i = 0
colors = ["red", "blue", "green", "pink", "cyan", "brown", "black", "purple", "yellow", "orange"]
# while n < 11:
#     t.pencolor(color[i])
#     for _ in range(n):
#         t.forward(100)
#         t.left(360 / n)
#     n += 1
#     i += 1

#random walk
directions = [0, 90, 180, 270]

# t.pensize(10)
# for i in range(100):
#     color = random.choice(colors)
#     t.pencolor(color)
#     direction = random.choice(directions)
#     t.forward(30)
#     t.left(direction)

# spiral
t.circle(100)
t.tiltangle(-10)
t.circle(100)
t.tiltangle(-20)
t.circle(100)
t.tiltangle(-30)
t.circle(100)
t.tiltangle(-40)
t.circle(100)
t.tiltangle(-50)
t.circle(100)
t.tiltangle(-60)
t.circle(100)
t.tiltangle(-70)
t.circle(100)
t.tiltangle(-80)
t.circle(100)
t.tiltangle(-90)


screen = Screen()
screen.exitonclick()
