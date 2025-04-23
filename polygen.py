import turtle
turtle.Screen().bgcolor("Blue")
turtle.Screen().setup(500,500)
t=turtle.Turtle()

num_sides=int(input("enter the number of sides you want for your polygon:"))
side_len=75
angle=360.0/num_sides
t.shape("classic")
t.pendown()
for i in range(num_sides):
    t.forward(side_len)
    t.right(angle)
turtle.done