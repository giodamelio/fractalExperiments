import turtle

# Make our screen
window = turtle.Screen()

# Make our canvas huge
window.screensize(10000, 10000)

# Make our screen draw faster
window.tracer(128, 1)

# Create first turtle
dragon = turtle.Turtle()
dragon.color("#FF4136")
dragon.hideturtle()

# Create second turtle
dragon2 = turtle.Turtle()
dragon2.color("#2ECC40")
dragon2.hideturtle()
dragon2.left(180)

# Draw our dragon
short = False
for n in range(1, 10000):
    # Move forward
    if short:
        dragon.forward(3)
        dragon2.forward(3)
    else:
        dragon.forward(5)
        dragon2.forward(5)

    # Toggle forward distance
    short = not short

    # Determine weather we should turn right or left
    if (((n & -n) << 1) & n) != 0:
        dragon.left(90)
        dragon2.left(90)
    else:
        dragon.right(90)
        dragon2.right(90)

# Wait for the user to click to exit
window.exitonclick()

