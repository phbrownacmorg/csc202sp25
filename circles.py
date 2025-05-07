import turtle

def draw_circle(radius: float, t: turtle.Turtle, fill: str | tuple[float, float, float] = 'white') -> None:
    orig_fill = t.fillcolor()
    orig_pen = t.pencolor()
    t.fillcolor(fill)
    if fill == 'black' or fill == (0, 0, 0):
        t.pencolor('white')
    t.up()
    t.forward(radius)
    t.left(90)
    t.down()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    # Put the turtle back as I found it
    t.up()
    t.right(90)
    t.backward(radius)
    t.down()
    t.fillcolor(orig_fill)
    if fill == 'black' or fill == (0, 0, 0):
        t.pencolor(orig_pen)

def draw_concentric_circles(radius: float, num_rings: float, t: turtle.Turtle) -> None:
    draw_circle(radius, t)
    if num_rings > 1:
        draw_concentric_circles(radius / num_rings * (num_rings - 1), num_rings - 1, t)

def draw_target(radius: float, num_rings: float, t: turtle.Turtle) -> None:
    colors: tuple[str,...] = ('yellow', 'red', 'blue', 'black', 'white')
    draw_circle(radius, t, colors[(num_rings - 1) // 2]) # type: ignore
    if num_rings > 1:
        draw_target(radius / num_rings * (num_rings - 1), num_rings - 1, t)

def main(args: list[str]) -> int:
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.speed(0)

    radius = 200

    draw_target(radius, 10, t)

    my_win.exitonclick()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))