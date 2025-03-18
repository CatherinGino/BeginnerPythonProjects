import turtle
import random

t = turtle.Turtle()
t.speed(100)
colors = ["red","yellow","pink","violet","purple","dark blue"]

for _ in range(36):
    t.color(random.choice(colors))
    t.circle(25)
    t.circle(50)
    t.circle(75)
    t.circle(100)
    t.right(10)

turtle.done()
