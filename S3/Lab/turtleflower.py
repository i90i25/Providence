petals =  int(input("Enter the number of petals: "))
import turtle
t = turtle.Turtle()
t.speed(0)
for i in range(petals):
    for j in range(2):
        t.circle(100,60)
        t.left(120)
    t.left(360/petals)
turtle.done()
