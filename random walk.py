import turtle
import random

t = turtle.Turtle()
t.speed(10)
colors = ["violet","indigo","blue","green","yellow","orange","red"]

for _ in range(100):
    t.color(random.choice(colors))
    t.forward(30)
    t.right(random.choice([0,90,180,270]))
