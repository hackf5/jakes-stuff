#! /usr/bin/env python3

import turtle

# Global Variables
size = 600
bricks_in_row = 8
bricks_in_col = 16
brick_width = size / bricks_in_row
brick_height = size / bricks_in_col
stagger_ratio = 0.7


def draw_brick(t: turtle.Turtle, w: float, h: float) -> None:
    current_heading = t.heading()

    for x in [(90, h), (0, w), (-90, h), (180, w)]:
        t.setheading(x[0])
        t.forward(x[1])

    t.setheading(current_heading)


def draw_row(t: turtle.Turtle, w: float, h: float, row_index: int) -> None:
    brick_count = bricks_in_row

    is_odd = row_index % 2 == 1
    if is_odd:
        brick_count = brick_count + 1

    for index in range(brick_count):
        bw = w

        if is_odd and index == 0:
            bw = stagger_ratio * w
        elif is_odd and index == (brick_count - 1):
            bw = (1 - stagger_ratio) * w

        draw_brick(t, bw, h)
        t.forward(bw)

    t.penup()
    t.goto(0, h * (row_index + 1))
    t.pendown()


def main() -> None:
    screen = turtle.Screen()
    screen.setup(width=size, height=size, startx=0, starty=0)
    screen.screensize(size, size)
    w, h = screen.screensize()
    screen.setworldcoordinates(0, 0, w, h)

    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(0)

    for row_index in range(bricks_in_col):
        draw_row(t, brick_width, brick_height, row_index)

    turtle.done()


if __name__ == "__main__":
    main()
