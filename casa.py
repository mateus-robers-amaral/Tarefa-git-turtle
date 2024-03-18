import turtle

def main():

    # inicial configs
    screen = turtle.setup(1920, 1080)
    screen = turtle.bgcolor("light blue")
    t = turtle.Turtle()
    turtle.title("Casa do Mateus")
    t.speed(5)
    t.shape("turtle")
    t.color("black")

    # construir a casa
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()

    t.goto(250, -200)
    t.goto(250, 50)
    t.goto(0, 50)
    t.goto(0, -200)

    t.penup()
    t.goto(250, -200)
    t.pendown()

    t.goto(450, -75)
    t.goto(450, 125)
    t.goto(250, 50)
    t.goto(250, -200)

    t.end_fill()

    t.penup()
    t.goto(0, 50)
    t.pendown()

    t.speed(5)
    #construir o telhado
    t.fillcolor("red")
    t.begin_fill()
    t.goto(125, 200)
    t.goto(250, 50)



    t.end_fill()

    t.hideturtle()
    turtle.done()

main()
