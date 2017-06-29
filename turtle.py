import turtle
import sys

steve = turtle.Turtle()

# draw a circle
def circle(size, color):
	steve.fillcolor(color)
	steve.begin_fill()
	steve.circle(size)
	steve.end_fill()

# draw a triangle
def triangle(size, color):
	steve.fillcolor(color)
	steve.begin_fill()
	x = 0
	while x < 3:
		steve.forward(size)
		steve.left(120)
		x += 1
	steve.end_fill()

# draw a star
def star(size, color):
	steve.fillcolor(color)
	steve.begin_fill()
	x = 0
	while x < 5:
		steve.forward(size)
		steve.left(144)
		x += 1
	steve.end_fill()

# user's choice - shapee, size, color
shape = raw_input("which shape do you want to draw? type either circle, triangle, or star >> ")
size = raw_input("what size do you want your shape to be? type from 50-200 >> ")
color = raw_input("what color do you want your shape to be? >> ")

# function with the correct perameter
if shape == "circle":
	circle(int(size), color)
elif shape == "triangle":
	triangle(int(size), color)
elif shape == "star":
	star(int(size), color)

turtle.done()