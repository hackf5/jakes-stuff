import math
import turtle

num_circles = 15
size = 1000
length_hyp = math.sqrt(2 * math.pow(size, 2))
radius = length_hyp / num_circles / 2


def circle_centered(t: turtle.Turtle, r: float) -> None:
    # preserve state
    pos = t.position()
    heading = t.heading()
    pen = t.isdown()

    t.penup()
    t.goto(pos[0], pos[1] - r)  # move down by r
    t.setheading(0)  # circle() assumes starting tangent is east
    if pen:
        t.pendown()
    t.circle(r)

    # restore state
    t.penup()
    t.goto(*pos)
    t.setheading(heading)
    if pen:
        t.pendown()


def draw_circle_line(t: turtle.Turtle, r: float) -> None:
    for _ in range(num_circles):
        t.penup()
        t.forward(r * 2)
        t.pendown()
        circle_centered(t, r)


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
    t.goto(0, 0)
    t.setheading(45)
    t.backward(radius)

    draw_circle_line(t, radius)

    t.penup()
    t.goto(0, h)
    t.setheading(-45)
    t.backward(radius)

    draw_circle_line(t, radius)

    turtle.done()


if __name__ == "__main__":
    main()
