import random
import turtle

def tree(branch_len: float, t: turtle.Turtle) -> None:
    min_branch: int = 6 # Minimum length of a branch in pixels
    fork_angle: int = 40 # angle between the two sides of a fork
    right_angle: float = fork_angle/2 * (0.5 + 0.5 * random.random()) # Angle between the parent and the right fork
    left_angle: float = fork_angle/2 * (0.5 + 0.5 * random.random()) # Angle between the parent and the left fork
    length_reduction: int = 12 # How much shorter the branch gets each time

    # Set the color according to how close we are to the leaves
    initial_color = t.pencolor()
    if branch_len < 2.5 * (min_branch + length_reduction):
        t.pencolor('green')

    # Set the thickness according to how deep we are in the tree
    initial_width = t.width()
    t.width(round(branch_len / length_reduction))

    if branch_len > min_branch:
        t.forward(branch_len)
        t.right(right_angle)
        tree(branch_len - length_reduction * (0.8 + 0.4 * random.random()), t)
        t.left(right_angle + left_angle)
        tree(branch_len - length_reduction * (0.8 + 0.4 * random.random()), t)
        t.right(left_angle)
        t.backward(branch_len)

    # Put the turtle back as we found it
    t.pencolor(initial_color)
    t.width(initial_width)


def main(args: list[str]) -> int:
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('brown')
    tree(75, t)
    my_win.exitonclick()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))