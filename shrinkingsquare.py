import turtle
turtle_screen=turtle.Screen()
turtle_screen.title("Turtle Pyhton")
turtle_screen.bgcolor("light green")

turtle_instance=turtle.Turtle()
turtle_instance.color("blue")

def ss(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size-=5

ss(150)
ss(130)
ss(110)
ss(90)
ss(80)
ss(60)
ss(40)
ss(20)
ss(10)

turtle.done()


