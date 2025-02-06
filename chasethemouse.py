from graphics import *
import math
from typing import cast
from button import make_button, inside

def almostEqual(a: float, b: float) -> bool:
    """Takes two floats A and B.  Returns True iff a and b
    are "almost" equal--that is, if A and B are within 0.000001
    of each other."""
    EPSILON: float = 0.0000001
    return abs(a - b) < EPSILON

def drawAnimal(animal: list[GraphicsObject], w: GraphWin) -> None:
    """Draw ANIMAL, represented as a list of GraphicsObjects."""
    # Pre: the parts of animal are not drawn
    for part in animal:
        part.draw(w)
    # Post: the parts of animal are all drawn on w

def getCenter(animal: list[GraphicsObject]) -> Point:
    """Get the center of ANIMAL, where the animal is represented as a list
    of GraphicsObjects and animal[0] has getCenter() defined."""
    # Pre:
    assert len(animal) > 0 and hasattr(animal[0], 'getCenter')
    # Post: return value is the center of animal[0]
    return cast(Circle, animal[0]).getCenter()

def moveAnimalTo(animal: list[GraphicsObject],
                 destination: Point) -> None:
    """Move ANIMAL (defined as a list of GraphicsObjects) so that the
    center of ANIMAL[0] is at DESTINATION."""
    # Pre:
    assert len(animal) > 0 and hasattr(animal[0], 'getCenter')
    # print(destination)
    currentLoc: Point = getCenter(animal)
    dx: float = destination.getX() - currentLoc.getX()
    dy: float = destination.getY() - currentLoc.getY()
    for part in animal:
        part.move(dx, dy)
    # Post: 
    # Using repr() is kind of cheating, but Point doesn't define ==
    assert almostEqual(getCenter(animal).getX(), destination.getX()) \
        and almostEqual(getCenter(animal).getY(), destination.getY())
    # ... and the rest of animal moved as well

def makeEyes(radius: float, color: str) -> list[GraphicsObject]:
    """Make and return a list of GraphicsObjects representing the eyes of an
    animal, where the radius of the animal's head is RADIUS and the eye color 
    is COLOR.  This function assumes that the center of the animal's head is at
    the origin."""
    # Pre:
    assert radius > 0 # and color actually gives a color
    eyeList: list[GraphicsObject] = []
    for x_sign in [-1, 1]:
        eye: Oval = Oval(Point(x_sign * 0.1 * radius, 0), Point(x_sign * 0.6 * radius, 0.7 * radius))
        eye.setFill(color)
        eyeList.append(eye)
    # Post:
    assert len(eyeList) == 2 and isinstance(eyeList[0], Oval) \
        and isinstance(eyeList[1], Oval) and \
        almostEqual(eyeList[0].getCenter().getX(), 
                    -(eyeList[1].getCenter().getX())) and \
        almostEqual(eyeList[0].getCenter().getY(), 
                    eyeList[1].getCenter().getY())
        # ... and their background colors match 'color' and 
    return eyeList

def makeMouseEars(radius: float, color: str) -> list[GraphicsObject]:
    """Make and return a list of GraphicsObjects representing mouse ears, where
    the radius of the mouse's head is RADIUS and the color of the ears is COLOR.
    This function assumes that the center of the mouse's head is at the origin."""
    # Pre:
    assert radius > 0 # and color actually gives a color
    earList: list[GraphicsObject] = []
    angle = math.radians(55)
    ear_radius = 0.6 * radius
    for x_sign in [-1, 1]:
        ear: Circle = Circle(Point(1.3 * radius * math.cos(angle) * x_sign,
                                   1.3 * radius * math.sin(angle)), ear_radius)
        ear.setOutline(color)
        ear.setFill(color)
        earList.append(ear)
    # Post:
    assert len(earList) == 2 and isinstance(earList[0], Circle) \
            and isinstance(earList[1], Circle) \
            and almostEqual(earList[0].getCenter().getX(), 
                            -(earList[1].getCenter().getX())) \
            and almostEqual(earList[0].getCenter().getY(), 
                    earList[1].getCenter().getY())
            # ... and the ears have the right color
    return earList

def makeCatEars(radius: float, color: str) -> list[GraphicsObject]:
    """Make and return a list of GraphicsObjects representing cat ears, where
    the radius of the cat's head is RADIUS and the color of the ears is COLOR.
    This function assumes that the center of the cat's head is at the origin."""
    # Pre:
    assert radius > 0 # and color actually gives a color
    earList: list[GraphicsObject] = []
    central_angle = math.radians(55)
    side_angle = math.radians(25)
    tip_radius = 1.8 * radius
    for x_sign in [-1, 1]:
        tip = Point(tip_radius * math.cos(central_angle) * x_sign,
                    tip_radius * math.sin(central_angle))
        top = Point(radius * math.cos(central_angle + side_angle) * x_sign,
                    radius * math.sin(central_angle + side_angle))
        bottom = Point(radius * math.cos(central_angle - side_angle) * x_sign,
                       radius * math.sin(central_angle - side_angle))
        ear = Polygon(tip, top, bottom)
        ear.setFill(color)
        ear.setOutline(color)
        earList.append(ear)
    # Post:
    assert len(earList) == 2 and isinstance(earList[0], Polygon) \
            and isinstance(earList[1], Polygon)
            # ... and the ears are symmetrical about Y and the proper color
    return earList

def makeMouth(radius: float) -> list[GraphicsObject]:
    """Make and return a list of GraphicsObjects representing the mouth of a
    cat or a mouse.  The radius of the animal's head is RADIUS.  This function
    assumes that the center of the animal's head is at the origin."""
    # Pre:
    assert radius > 0
    lines: list[GraphicsObject] = []
    angle = math.radians(-55)
    length = 0.6
    for x_sign in [-1, 1]:
        line = Line(Point(0, -0.3 * radius), 
                    Point(length * radius * math.cos(angle) * x_sign,
                          length * radius * math.sin(angle)))
        lines.append(line)
    # Post:
    assert len(lines) == 2 and isinstance(lines[0], Line) \
        and isinstance(lines[1], Line)
        # ... and the lines are symmetric about Y
    return lines

def makeNose(radius: float, color: str) -> Polygon:
    """Make and return a Polygon representing the mouth of a cat or a mouse.
    The radius of the animal's head is RADIUS.  This function assumes that
    the center of the animal's head is at the origin."""
    # Pre:
    assert radius > 0 # and color actually gives a color
    size = 0.3
    nose = Polygon(Point(0, -size * radius),
                   Point((-size/2) * radius, 0),
                   Point((size/2) * radius, 0))
    nose.setFill(color)
    # Post:
    assert(len(nose.getPoints()) == 3) # nose is a triangle
    # ... and nose is symmetric about the Y axis 
    # ... and nose is the right color
    return nose

def makeWhiskers(radius: float) -> list[GraphicsObject]:
    """Make and return a list of GraphicsObjects representing the whiskers of a
    cat or a mouse.  The radius of the animal's head is RADIUS.  This function
    assumes that the center of the animal's head is at the origin."""
    # Pre:
    assert radius > 0
    whiskerList: list[GraphicsObject] = []
    inner_r = 0.7
    outer_r = 1.7
    angle = math.radians(10)
    for x_sign in [1, -1]:
        for i in [-1, 0, 1]:
            whisker = Line(Point(x_sign * inner_r * radius * math.cos(i * angle),
                                 inner_r * radius * math.sin(i * angle)),
                           Point(x_sign * outer_r * radius * math.cos(i * angle),
                                 outer_r * radius * math.sin(i * angle)))
            whiskerList.append(whisker)
    # Post:
    assert len(whiskerList) == 6 
    # ... and everything in whiskerList is a Line
    # ... and whiskerList[i] and whiskerList[i+3] are symmetric about Y
    #     for 0 <= i < 3
    return whiskerList

def makeHead(radius: float, color: str) -> Circle:
    """Make and return a Circle representing the head of an animal.  The radius
    of the animal's head is RADIUS.  This function assumes that the center of
    the animal's head is at the origin."""
    # Pre:
    assert radius > 0 # and color actually gives a color
    head = Circle(Point(0, 0), radius)
    head.setFill(color)
    head.setOutline(color)
    # Post:
    assert head.getRadius() == radius and \
        almostEqual(head.getCenter().getX(), 0) and \
        almostEqual(head.getCenter().getY(), 0)
    # ... and head is the correct color
    return head

def makeMouse(radius: float) -> list[GraphicsObject]:
    """Make and return a list of GraphicsObjects representing a mouse.  The radius
    of the animal's head is RADIUS.  This function assumes that the center of
    the animal's head is at the origin."""
    # Pre:
    assert radius > 0
    result: list[GraphicsObject] = [makeHead(radius, 'gray')]
    result.extend(makeMouseEars(radius, 'gray'))
    result.extend(makeEyes(radius, 'black'))
    result.extend(makeMouth(radius))
    result.append(makeNose(radius, 'black'))
    result.extend(makeWhiskers(radius))
    return result

def makeCat(radius: float) -> list[GraphicsObject]:
    """Make and return a list of GraphicsObjects representing a mouse.  The radius
    of the animal's head is RADIUS.  This function assumes that the center of
    the animal's head is at the origin."""
    # Pre:
    assert radius > 0
    result: list[GraphicsObject] = [makeHead(radius, 'orange')]
    result.extend(makeCatEars(radius, 'orange'))
    result.extend(makeEyes(radius, 'green'))
    result.extend(makeMouth(radius))
    result.append(makeNose(radius, 'black'))
    result.extend(makeWhiskers(radius))
    # Post:
    assert len(result) == 14 and hasattr(result[0], 'getCenter')
    # ... and the parts all have a fillColor of color
    return result

def caught(predator: list[GraphicsObject], prey: list[GraphicsObject]) -> bool:
    """Returns True if the distance between predator and prey is less than the
    radius of the predator (that is, the predator has caught the prey)."""
    # Pre:
    assert len(predator) > 0 and len(prey) > 0 \
        and hasattr(predator[0], 'getRadius') \
        and hasattr(predator[0], 'getCenter') \
            and hasattr(prey[0], 'getCenter')
    predatorPt = getCenter(predator)
    preyPt = getCenter(prey)
    distance = math.sqrt((predatorPt.getX() - preyPt.getX())**2 + 
                         (predatorPt.getY() - preyPt.getY())**2)
    # Post:
    # Return value is True iff radius of predator > distance between
    #    predator and prey
    return distance < cast(Circle, predator[0]).getRadius()


def main(args: list[str]) -> int:
    w: GraphWin = GraphWin('Graphics window', 800, 800)
    # Rearrange the coordinate system to be easier to think about.
    # X increases to the right, Y increases up.  The origin is in
    # the center, and the absolute value of any coordinate tells you
    # proportionally how close it is to the edge.
    # The layout of the picture no longer depends on the size of
    # the window (it will scale to any size).
    w.setCoords(-1, -1, 1, 1)

    quit_button = make_button(w, Point(-1, 1), Point(-.8, .8),
                            'Quit')

    mouse: list[GraphicsObject] = makeMouse(0.05)
    drawAnimal(mouse, w)
    cat: list[GraphicsObject] = makeCat(0.2)
    moveAnimalTo(cat, Point(2, 0))
    drawAnimal(cat, w)

    # DRAW STUFF HERE
    # Chase the mouse for 5 mouse clicks
    distance = 2
    click = w.getMouse()
    while not inside(quit_button, click) and not caught(cat, mouse):
        mousePt = getCenter(mouse)
        moveAnimalTo(mouse, click)
        moveAnimalTo(cat, mousePt)
        click = w.getMouse() # MUST update the variable used in the loop condition

    # Force the window to stay open until we click
    #w.getMouse()
    w.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))