import turtle

turtle_screen=turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Python Turtle")


turtle_instance=turtle.Turtle()
turtle.speed(0)                   # en hizli
turtle_colors=["red","blue","green","orange","purple"]

for i in range(10):
    turtle_instance.color(turtle_colors[i%5])
    turtle_instance.circle(10*i)
    turtle_instance.circle(-10*i)
    turtle_instance.left(i)


turtle.mainloop()