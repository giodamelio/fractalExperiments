import turtle

# Make our screen
window = turtle.Screen()

# Make our canvas huge
window.screensize(10000, 10000)

# Make our screen draw faster
window.delay(1)

# Create our turtle
dragon = turtle.Turtle()

# Make our turtle fast
dragon.speed("fastest")

# Hide our turtle
dragon.hideturtle()

# Draw our dragon
for n in range(1, 1000):
    # Move forward 50
    dragon.forward(10)

    # Determine weather we should turn right or left
    if (((n & -n) << 1) & n) != 0:
        dragon.left(90)
    else:
        dragon.right(90)

# Wait for the user to click to exit
window.exitonclick()

