#! /usr/bin/env python3

import turtle

# Global variables
size = 600
squares_on_axis = 8
length_of_square_side = size / squares_on_axis


def draw_square(t: turtle.Turtle, side_length: float, is_white: bool) -> None:
    current_heading = t.heading()

    t.begin_poly()
    t.begin_fill()

    if is_white:
        t.fillcolor(1, 1, 1)
    else:
        t.fillcolor(0, 0, 0)

    for to_angle in [90, 0, -90, 180]:
        t.setheading(to_angle)
        t.forward(side_length)

    t.end_fill()
    t.end_poly()

    t.setheading(current_heading)


def draw_row_of_squares(t: turtle.Turtle, side_length: float, row_index: int) -> None:
    for column_index in range(squares_on_axis):
        is_white = column_index % 2 == row_index % 2
        draw_square(t, side_length, is_white)
        t.forward(side_length)

    t.penup()
    t.goto(0, side_length * (row_index + 1))
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

    for row_index in range(squares_on_axis):
        draw_row_of_squares(t, length_of_square_side, row_index)

    turtle.done()


if __name__ == "__main__":
    main()
