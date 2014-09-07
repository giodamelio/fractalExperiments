import turtle

# Make our screen
window = turtle.Screen()

# Make our screen draw faster
window.delay(5)

# Create our turtle
dragon = turtle.Turtle()

# Hide our turtle
dragon.hideturtle()

# Draw a square
dragon.forward(50)
dragon.left(90)
dragon.forward(50)
dragon.left(90)
dragon.forward(50)
dragon.left(90)
dragon.forward(50)
dragon.left(90)

# Wait for the user to click to exit
window.exitonclick()

