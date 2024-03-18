import turtle

def main():

    # configs iniciais
    screen = turtle.setup(1366, 768)
    screen = turtle.bgcolor("light blue")
    t = turtle.Turtle()
    turtle.title("Casa do Mateus")
    t.speed(5)
    t.shape("turtle")
    t.color("black")

    # desenhar o chão
    t.penup()
    t.goto(-960, 62.5)
    t.pendown()
    t.fillcolor("#267F00")
    t.begin_fill()  

    t.goto(960, 62.5)
    t.goto(960, -560)
    t.goto(-960, -560)
    t.goto(-960, 62.5)

    t.end_fill()

    # desenhar a casa
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

    # desenhar o telhado
    t.fillcolor("red")
    t.begin_fill()
    t.goto(125, 200)
    t.goto(250, 50)

    t.penup()
    t.goto(125, 200)
    t.pendown()

    t.goto(325, 250)
    t.goto(450, 125)
    t.goto(250, 50)

    t.end_fill()

    # desenhar a porta
    t.fillcolor("brown")
    t.begin_fill()

    t.penup()
    t.goto(50, -50)
    t.pendown()

    t.goto(150, -50)
    t.goto(150, -200)
    t.goto(50, -200)
    t.goto(50, -50)

    t.end_fill()

    # desenhar a maçaneta
    t.penup()
    t.goto(125, -150)
    t.pendown() 

    t.fillcolor("#C49C5C")
    t.begin_fill()
    t.circle(7.5)

    t.end_fill()

    # desenhar a árvore


    t.hideturtle()
    turtle.done()

main()