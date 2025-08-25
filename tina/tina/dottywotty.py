#! /usr/bin/env python3
import turtle

size = 600
cell_count = 20
length_of_cell_side = size / cell_count
dot_size = 20


def make_J():
    coords = set()

    # dimensions
    top = 18  # 1 below top edge
    bottom = 1  # 1 above bottom edge
    left = 5
    right = 14
    thickness = 3

    # top bar
    for y in range(top - thickness + 1, top + 1):
        for x in range(2, right + 1):
            coords.add((x, y))

    # vertical stem
    for x in range(right - thickness + 1, right + 1):
        for y in range(bottom + thickness, top + 1):
            coords.add((x, y))

    # bottom hook
    for y in range(bottom, bottom + thickness):
        for x in range(left, right + 1):
            coords.add((x, y))

    coords.remove((5, 1))
    coords.remove((5, 3))
    coords.remove((14, 1))

    return coords


J_coords = make_J()


def draw_cell(
    t: turtle.Turtle, side_length: float, dot_size: int, pos: tuple[int, int]
) -> None:
    if pos in J_coords:
        return

    current_heading = t.heading()
    current_position = t.position()

    for heading in [90, 0]:
        t.setheading(heading)
        t.forward(side_length / 2)

    t.pendown()
    t.dot(dot_size)
    t.penup()
    t.setheading(current_heading)
    t.goto(current_position)


def draw_row(
    t: turtle.Turtle, side_length: float, dot_size: int, row_index: int
) -> None:
    for column_index in range(cell_count):
        draw_cell(t, side_length, dot_size, (column_index, row_index))
        t.forward(side_length)

    t.goto(0, side_length * (row_index + 1))


def main() -> None:
    screen = turtle.Screen()
    screen.setup(width=size, height=size, startx=0, starty=0)
    screen.screensize(size, size)
    w, h = screen.screensize()
    screen.setworldcoordinates(0, 0, w, h)

    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(0)
    t.penup()

    for row_index in range(cell_count):
        draw_row(t, length_of_cell_side, dot_size, row_index)

    turtle.done()


if __name__ == "__main__":
    main()
