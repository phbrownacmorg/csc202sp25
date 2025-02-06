from graphics import *

def inside(rect: Rectangle, pt: Point) -> bool:
    """Return True iff PT is inside RECT."""
    p1 = rect.getP1()
    p2 = rect.getP2()
    minX = min(p1.getX(), p2.getX())
    maxX = max(p1.getX(), p2.getX())
    minY = min(p1.getY(), p2.getY())
    maxY = max(p1.getY(), p2.getY())
    return minX < pt.getX() < maxX and minY < pt.getY() < maxY

def make_button(w: GraphWin, p1: Point, p2: Point, text: str) -> Rectangle:
    """Make and return a Rectangle defined by P1 and P2, representing a button.
    The button displays TEXT as its legend, and is drawn on W."""
    button: Rectangle = Rectangle(p1, p2)
    button.draw(w)
    label = Text(button.getCenter(), text)
    label.draw(w)
    return button

def main(args: list[str]) -> int:
    w: GraphWin = GraphWin('Graphics window', 800, 800)
    # Rearrange the coordinate system to be easier to think about.
    # X increases to the right, Y increases up.  The origin is in
    # the center, and the absolute value of any coordinate tells you
    # proportionally how close it is to the edge.
    # The layout of the picture no longer depends on the size of
    # the window (it will scale to any size).
    w.setCoords(-1, -1, 1, 1)

    button: Rectangle = make_button(w, Point(-1, 1), Point(-.8, .8),
                                    'Quit')
    instructions: Text = Text(Point(0, -0.8), 
                              'Click in the Quit button to quit')
    instructions.draw(w)
    clickLabel: Text = Text(Point(0, -0.9), '')
    clickLabel.draw(w)

    for i in range(10000):
        click: Point = w.getMouse()
        clickLabel.setText('({:.2f}, {:.2f})'.format(click.getX(), click.getY()))
        if inside(button, click):
            instructions.setText('Click once more to exit')
            break

    # Force the window to stay open until we click
    w.getMouse()
    w.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))