import turtle
import math

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
turtle.bgcolor("black")
t.color("yellow")

for i in range(100):
    angle = i*137.5
    radius = i
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))

    t.penup()
    t.goto(x,y)
    t.pendown()
    t.dot(10)
