# author: erictheballer

import turtle

n = 
length = 125
angle = 180 - 180 * (n-2) / n
numbers = range(0, n)

tyrone = turtle.Turtle()

for number in numbers:
	tyrone.color("#FF04C1")
	tyrone.forward(length)
	tyrone.left(angle)
	