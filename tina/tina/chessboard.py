#! /usr/bin/env python3

import turtle

# Global variables
size = 600
squares_on_axis = 300
length_of_square_side = size / squares_on_axis


def draw_square(t: turtle.Turtle, l: float, is_white: bool):
    current_heading = t.heading()

    t.begin_poly()
    t.begin_fill()

    if is_white:
        t.fillcolor(1, 1, 1)
    else:
        t.fillcolor(0, 0, 0)

    for to_angle in [90, 0, -90, 180]:
        t.setheading(to_angle)
        t.forward(l)

    t.end_fill()
    t.end_poly()

    t.setheading(current_heading)


def draw_row_of_squares(t: turtle.Turtle, l: float, row_index: int):
    for column_index in range(squares_on_axis):
        is_white = column_index % 2 == row_index % 2
        draw_square(t, l, is_white)
        t.forward(l)

    t.penup()
    t.goto(0, l * (row_index + 1)) 
    t.pendown()

    
def main():
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