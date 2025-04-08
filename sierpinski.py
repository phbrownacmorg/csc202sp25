import turtle

def draw_triangle(size: float, fillcolor: str, t: turtle.Turtle) -> None:
    """Draw a triangle of length SIZE, filled in FILLCOLOR, using turtle T.
       Assumes that T is initially at one corner of the triangle with its
       pen *up*, and that the triangle will be drawn to the turtle's left
       of the turtle's initial direction.  The turtle is returned in the
       same position and state as it started."""
    old_fill: str | tuple[float, float, float] = t.fillcolor()
    t.fillcolor(fillcolor)
    t.down()
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()
    t.up()
    # Turtle is back in its starting position, same orientation, pen up
    # Just restore the fillcolor (not strictly needed, but safer)
    t.fillcolor(old_fill)


def sierpinski(size: float, degree: int, t: turtle.Turtle) -> None:
    """Draw a Sierpinski triangle of size SIZE and degree DEGREE using turtle T.
       Assumes that the turtle is initially at one corner of the triangle. The
       triangle will be drawn to the turtle's left of its initial direction.
       Assumes that the turtle initially has the pen *up*, not down."""
    colormap = ("blue", "red", "green", "white", "yellow", "violet", "orange")
    draw_triangle(size, colormap[degree], t)
    if degree > 0:
        # Draw three smaller triangles in the corners
        for i in range(3):
            sierpinski(size/2, degree - 1, t)
            t.forward(size)
            t.left(120)

def main(args: list[str]) -> int:
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.speed(0)

    size = 400

    # Go to a corner and set up to start
    t.up()
    t.left(90)
    t.forward(size / 2)
    t.left(150)

    sierpinski(size, 6, t)
    
    my_win.exitonclick()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))