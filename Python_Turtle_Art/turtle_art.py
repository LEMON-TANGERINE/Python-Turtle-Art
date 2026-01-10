import turtle
# 0) Create a background
screen = turtle.Screen()
screen.bgcolor("black")

# 1) Create the "pen"
t = turtle.Turtle()
t.speed(0)
t.pensize(3)

# 2) Prepare a list of colors to cycle through
colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

# 3) Draw a square spiral
distance = 5
for i in range(250):
    t.pencolor(colors[i % len(colors)])
    t.forward(distance)
    t.right(90)
    distance += 3

turtle.done()