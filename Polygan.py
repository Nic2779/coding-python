import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()

sum_sides = 6
side_length = 70
angle = 360.0 / sum_sides

for i in range(sum_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done
