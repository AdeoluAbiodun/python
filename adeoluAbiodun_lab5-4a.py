import turtle

# Set up turtle
t = turtle.Turtle()
t.speed(3)

# Function to draw a circle for snowman parts
def draw_circle(x, y, radius):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(radius)

# Function to draw the base of the snowman
def drawBase():
    draw_circle(0, -150, 60)

# Function to draw the midsection of the snowman
def drawMidSection():
    draw_circle(0, -40, 45)

# Function to draw the head of the snowman with facial features
def drawHead():
    draw_circle(0, 50, 30)
    
    # Draw eyes
    t.penup()
    t.goto(-10, 80)
    t.pendown()
    t.dot(5)
    
    t.penup()
    t.goto(10, 80)
    t.pendown()
    t.dot(5)
    
    # Draw mouth
    t.penup()
    t.goto(-10, 65)
    t.pendown()
    t.setheading(-60)
    for _ in range(5):
        t.forward(5)
        t.left(30)

# Function to draw the snowman's arms
def drawArms():
    t.penup()
    t.goto(-45, 10)
    t.pendown()
    t.setheading(160)
    t.forward(50)
    
    t.penup()
    t.goto(45, 10)
    t.pendown()
    t.setheading(20)
    t.forward(50)

# Function to draw the snowman's hat
def drawHat():
    # Draw hat base
    t.penup()
    t.goto(-25, 90)
    t.pendown()
    t.forward(50)
    
    # Draw top of hat
    t.penup()
    t.goto(-15, 100)
    t.pendown()
    t.setheading(70)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(30)

# Main function
def main():
    # Draw all parts of the snowman
    drawBase()
    drawMidSection()
    drawHead()
    drawArms()
    drawHat()
    
    # Keep the window open until clicked
    turtle.done()

# Run the main function
if __name__ == "__main__":
    main()
