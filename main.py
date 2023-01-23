"""Main Function"""
import turtle


tim = turtle.Turtle()
my_screen = turtle.Screen()


def move_up():
    """Function to instruct turtle to move forward"""
    tim.setheading(90)
    tim.forward(10)


def move_down():
    """Function to instruct turtle to move forward"""
    tim.setheading(270)
    tim.forward(10)


def move_right():
    """Function to instruct turtle to move forward"""
    tim.setheading(180)
    tim.forward(10)


def move_left():
    """Function to instruct turtle to move forward"""
    tim.setheading(0)
    tim.forward(10)


def clear_screen():
    """Function to clear screen"""
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



my_screen.listen()
my_screen.onkey(move_up, 'i')
my_screen.onkey(move_down, 'k')
my_screen.onkey(move_left, 'l')
my_screen.onkey(move_right, 'j')
my_screen.onkey(clear_screen, 'c')

my_screen.exitonclick()
