import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

my_turtle = turtle.Turtle()
my_turtle.pensize(3)
my_turtle.color("black")
my_turtle.speed(2)

side_length = 100

for _ in range(4):
    my_turtle.forward(side_length)
    my_turtle.right(90)
