# Name: Adeolu Abiodun  ||  Date: 08/18/2024  ||  Program file: adeoluAbiodun_lab3-1.py

# Program Description/Purpose: This program calculates the total cost, applicable discount, both due sales tax and the total amount.

#Constant variable
import turtle

t = turtle.Turtle()

# Draw the 100px square
for _ in range(4):
    t.forward(100)
    t.right(90)

# Move the turtle to draw the circle
t.penup()
t.goto(50, -80)
t.pendown()

# Draw 80px circle and fill it with red
t.color("red")
t.begin_fill()
t.circle(80)
t.end_fill()