import turtle
import random
# Initialization ... Please adjust the parameters in window.setup to fit your display.
window = turtle.Screen()
window.setup(1900, 1000, startx=0, starty=0)
window.bgcolor("black")
myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)
myPen.pensize(1)


def random_color():
    # Provides RGB color string used by Turtle to change the color of each spiroburst.
    color_string = ""
    r = hex(random.randint(16, 255))
    g = hex(random.randint(16, 255))
    b = hex(random.randint(16, 255))
    color_string = "#" + r[2:] + g[2:] + b[2:]
    # Return a string with a hexadecimal code in format, #nnnnnn, n = 10-FF (16-255)
    return color_string


def random_placement():
    # Provides random coordinates to place each spiroburst.
    # Please note: the ranges specified may not work with your display.
    x = random.randint(-800, 800)
    y = random.randint(-400, 400)
    return x, y


def draw_spiroburst():
    #Draws a spiroburst on the screen using randomly generated parameters.
    f_select = [10,20,30,45,60]
    myPen.penup()
    myPen.color(random_color())
    myPen.goto(random_placement())
    radius = random.randint(20, 90)
    length = random.randint(30, 380)
    factor = random.choice(f_select)
    for _ in range(360//factor):
        myPen.pendown()
        myPen.circle(radius,length)
        myPen.penup()
        myPen.circle(radius,-length)
        myPen.lt(factor)


def main() -> None:
    """
    Main function: invokes the draw_spiroburst function in a loop.
    The range number determines the number of spirobursts that are drawn on the screen.
    """
    for _ in range(10):
        draw_spiroburst()
    turtle.mainloop()

if __name__ == '__main__':
    main()
