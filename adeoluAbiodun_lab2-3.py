# Name: Adeolu Abiodun  ||  Date: 08/21/2024  || Program File: adeoluAbiodun_lab2-3.py
# Program Description/Purpose: This program draws a square that is 100 pixels wide on each side and a circle with radius 80 pixels  filled with red color that is centered inside the square.

import turtle

t = turtle.Turtle()

# Draw the 100px square
for _ in range(4):
    t.forward(100)
    t.right(90)

# Draw the circle
t.penup()
t.goto(50, -80)
t.pendown()

# Draw 80px circle fill with red color
t.color("red")
t.begin_fill()
t.circle(80)
t.end_fill()