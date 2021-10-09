from turtle import Turtle, Screen

turtles = []
place = 0


for _ in range(3):
    turtle = Turtle(shape="square")
    turtle.color("white")
    turtle.sety(0)
    turtle.setx(place)
    place -= 20
    turtles.append(turtle)


window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("My snake game")
window.exitonclick()

game_is_on = True

while game_is_on:
    for turtle in turtles:
        turtle.forward(20)


