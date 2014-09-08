def screenshot():
    print("Saved")
    window.getcanvas().postscript(file="test.eps")
window.onkey(screenshot, "space")
window.listen()

