import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("#F6FDC3")
drawing_board.title("Drawing Game")

turtle_instance = turtle.Turtle()

def turtle_writing():
    turtle_instance.forward(100)
def turtle_turn_left():
    turtle_instance.left(10)
def turtle_turn_right():
    turtle_instance.right(10)
def turtle_clear():
    turtle_instance.clear()
def turtle_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()
def turtle_penup():
    turtle_instance.penup()
def turtle_pendown():
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun=turtle_writing,key="space")
drawing_board.onkey(fun=turtle_turn_left,key="Up")
drawing_board.onkey(fun=turtle_turn_right,key="Down")
drawing_board.onkey(fun=turtle_clear,key="c")
drawing_board.onkey(fun=turtle_home,key="h")
drawing_board.onkey(fun=turtle_penup,key="w")
drawing_board.onkey(fun=turtle_pendown,key="r")

turtle.mainloop()