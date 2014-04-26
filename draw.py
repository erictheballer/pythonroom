# author: erictheballer

import turtle

angle = 90
numbers = range(10, 200, 3)
colors = ["red", "blue", "yellow", "green"]

tyrone = turtle.Turtle()

for number in numbers:
	for color in colors:
		tyrone.color(color)
		tyrone.forward(number)
		tyrone.left(angle)
	tyrone.left(8)
			