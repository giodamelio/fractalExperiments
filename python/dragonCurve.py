import turtle

# Make our screen
window = turtle.Screen()

# Make our canvas huge
window.screensize(10000, 10000)

# Make our screen draw faster
window.tracer(128, 1)

# Create first turtle
dragon1 = turtle.Turtle()
dragon1.color("#FF4136")
dragon1.hideturtle()

# Create second turtle
dragon2 = turtle.Turtle()
dragon2.color("#2ECC40")
dragon2.hideturtle()
dragon2.left(90)

# Create third turtle
dragon3 = turtle.Turtle()
dragon3.color("#0074D9")
dragon3.hideturtle()
dragon3.left(180)

# Create forth turtle
dragon4 = turtle.Turtle()
dragon4.color("#FFDC00")
dragon4.hideturtle()
dragon4.left(270)

# Draw our dragon
short = False
for n in range(1, 10000):
    # Move forward
    if short:
        dragon1.forward(3)
        dragon2.forward(5)
        dragon3.forward(3)
        dragon4.forward(5)
    else:
        dragon1.forward(5)
        dragon2.forward(3)
        dragon3.forward(5)
        dragon4.forward(3)

    # Toggle forward distance
    short = not short

    # Determine weather we should turn right or left
    if (((n & -n) << 1) & n) != 0:
        dragon1.left(90)
        dragon2.left(90)
        dragon3.left(90)
        dragon4.left(90)
    else:
        dragon1.right(90)
        dragon2.right(90)
        dragon3.right(90)
        dragon4.right(90)

# Wait for the user to click to exit
window.exitonclick()

