import turtle

t = turtle.Turtle()
t.speed(0)
t.color("dark blue")

for i in range(100):
    t.forward(i*2)
    t.right(91)

turtle.done()
