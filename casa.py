import turtle

def main():

    # configs iniciais
    screen = turtle.setup(1366, 768)
    screen = turtle.bgcolor("#1E90FF")
    t = turtle.Turtle()
    turtle.title("Casa do Mateus")
    t.speed(0)
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

    # detalhes de tijolos
    t.penup()
    t.goto(250, 50)
    t.pendown()

    t.goto(180, 50)
    t.goto(180, 25)
    t.goto(250, 25)
    t.goto(250, 50)

    t.penup()
    t.goto(200, 25)
    t.pendown()

    t.goto(200, 25)
    t.goto(200, 0)
    t.goto(250, 0)
    t.goto(250, 25)

    t.penup()
    t.goto(250, -150)
    t.pendown()

    t.goto(285, -125)
    t.goto(285, -150)
    t.goto(250, -175)

    t.goto(250, -125)
    t.goto(268, -112.5)
    t.goto(268, -138)

    # desenhar o telhado
    t.penup()
    t.goto(0, 50)
    t.pendown()

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

    # desenhar as janelas
    t.penup()
    t.goto(295, -95)
    t.pendown()

    t.fillcolor("#DAA520")
    t.begin_fill()

    t.goto(420, -28)
    t.goto(420, 55)
    t.goto(295, -5)
    t.goto(295, -95)

    t.end_fill()

    t.penup()
    t.goto(355, 24)
    t.pendown()

    t.color("black")
    t.goto(355, -64)

    t.penup()
    t.goto(345, -34)
    t.pendown()

    t.circle(3)

    t.penup()
    t.goto(365, -26)
    t.pendown()

    t.circle(3)

    t.penup()
    t.goto(125, 70)
    t.pendown()

    t.fillcolor("#DAA520")
    t.begin_fill()
    t.circle(35)

    t.end_fill()

    t.penup()
    t.goto(125, 138)
    t.pendown()

    t.color("black")
    t.goto(125, 70)

    t.penup()
    t.goto(90, 104)
    t.pendown()

    t.goto(160, 104)

    # desenhar a porta
    t.penup()
    t.goto(50, -50)
    t.pendown()

    t.fillcolor("brown")
    t.begin_fill()

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

    # desenhar a lua
    t.penup()
    t.goto(-400, 200)
    t.pendown()

    t.fillcolor("#FFD700")
    t.begin_fill()
    t.circle(75)

    t.end_fill()

    t.penup()
    t.goto(-475, 200)
    t.pendown()

    t.color("#1E90FF")
    t.fillcolor("#1E90FF")
    t.begin_fill()
    t.circle(85)

    t.end_fill()

    # desenhar a estrelas
    t.penup()
    t.goto(-200, 250)
    t.pendown()

    t.color("#FFD700")
    t.fillcolor("#FFD700")
    t.begin_fill()

    for i in range(5):
        t.forward(22)
        t.right(144)

    t.end_fill()

    t.penup()
    t.goto(-150, 290)
    t.pendown()

    t.begin_fill()

    for i in range(5):
        t.forward(15)
        t.right(144)

    t.end_fill()

    t.penup()
    t.goto(-180, 180)
    t.pendown()

    t.begin_fill()

    for i in range(5):
        t.forward(24)
        t.right(144)

    t.end_fill()

    t.penup()
    t.goto(280, 320)
    t.pendown()

    t.begin_fill()

    for i in range(5):
        t.forward(18)
        t.right(144)

    t.end_fill()

    t.penup()
    t.goto(480, 335)
    t.pendown()

    t.begin_fill()

    for i in range(5):
        t.forward(16)
        t.right(144)

    t.end_fill()

    t.penup()
    t.goto(380, 315)
    t.pendown()

    t.begin_fill()

    for i in range(5):
        t.forward(23)
        t.right(144)

    t.end_fill()

    t.penup()
    t.goto(0, 235)
    t.pendown()

    t.begin_fill()

    for i in range(5):
        t.forward(14)
        t.right(144)

    t.end_fill()

    t.penup()
    t.goto(-45, 135)
    t.pendown()

    t.begin_fill()

    for i in range(5):
        t.forward(12)
        t.right(144)

    t.end_fill()

    t.penup()
    t.goto(-530, 235)
    t.pendown()

    t.begin_fill()

    for i in range(5):
        t.forward(23)
        t.right(144)

    t.end_fill()

    t.penup()
    t.goto(-500, 335)
    t.pendown()

    t.begin_fill()

    for i in range(5):
        t.forward(18)
        t.right(144)

    t.end_fill()

    t.penup()
    t.goto(-430, 155)
    t.pendown()

    t.begin_fill()

    for i in range(5):
        t.forward(21)
        t.right(144)

    t.end_fill()

    t.penup()
    t.goto(125, 280)
    t.pendown()

    t.begin_fill()

    for i in range(5):
        t.forward(21)
        t.right(144)

    t.end_fill()

    t.penup()
    t.goto(500, 280)
    t.pendown()

    t.begin_fill()

    for i in range(5):
        t.forward(23)
        t.right(144)

    t.end_fill()

    t.penup()
    t.goto(580, 170)
    t.pendown()

    t.begin_fill()

    for i in range(5):
        t.forward(15)
        t.right(144)

    t.end_fill()

    t.penup()
    t.goto(630, 330)
    t.pendown()

    t.begin_fill()

    for i in range(5):
        t.forward(18)
        t.right(144)

    t.end_fill()

    # desenhar a árvore
        # tronco
    t.color("black")
    t.penup()
    t.goto(-300, -250)
    t.pendown()

    t.fillcolor("#A0522D")
    t.begin_fill()

    t.goto(-300, -30)
    t.goto(-250, -30)
    t.goto(-250, -250)
    t.goto(-300, -250)

    t.end_fill()

        # galho esquerda
    t.penup()
    t.goto(-300, -40)
    t.pendown()

    t.fillcolor("#A0522D")
    t.begin_fill()

    t.goto(-280, -30)
    t.goto(-380, -10)
    t.goto(-400, -20)
    t.goto(-300, -40)

    t.end_fill()
        #galho direita
    t.penup()
    t.goto(-250, -40)
    t.pendown()

    t.fillcolor("#A0522D")
    t.begin_fill()

    t.goto(-270, -30)
    t.goto(-160, -10)
    t.goto(-140, -20)
    t.goto(-250, -40)

    t.end_fill()

        # galho centro-esquerda
    t.penup()
    t.goto(-290, -35)
    t.pendown()

    t.fillcolor("#A0522D")
    t.begin_fill()

    t.goto(-280, -30)
    t.goto(-285, 15)
    t.goto(-290, 10)
    t.goto(-290, -35)

    t.end_fill()

        # galho centro-direita
    t.penup()
    t.goto(-260, -35)
    t.pendown()

    t.fillcolor("#A0522D")
    t.begin_fill()

    t.goto(-275, -30)
    t.goto(-250, 15)
    t.goto(-250, 10)
    t.goto(-260, -35)

    t.end_fill()

        # desenhar as folhas
    t.speed(100)
    t.penup()
    t.goto(-400, -20)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#32CD32")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()

    t.penup()
    t.goto(-410, -40)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#32CD32")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()

    t.penup()
    t.goto(-380, -40)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#9ACD32")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()

    t.penup()
    t.goto(-440, -20)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#32CD32")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()

    t.penup()
    t.goto(-420, 10)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#32CD32")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()
    
    t.penup()
    t.goto(-380, 10)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#9ACD32")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()
        
    t.penup()
    t.goto(-410, 20)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#32CD32")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()

    t.penup()
    t.goto(-285, 15)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#32CD32")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()

    t.penup()
    t.goto(-320, 15)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#FFA500")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()

    t.penup()
    t.goto(-255, 15)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#32CD32")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()

    t.penup()
    t.goto(-255, 45)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#32CD32")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()

    t.penup()
    t.goto(-320, 45)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#32CD32")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()

    t.penup()
    t.goto(-290, 45)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#FFA500")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()

    t.penup()
    t.goto(-300, 60)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#9ACD32")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()

    t.penup()
    t.goto(-250, 60)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#32CD32")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()

    t.penup()
    t.goto(-200, 45)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#9ACD32")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()

    t.penup()
    t.goto(-180, 35)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#FFA500")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()

    t.penup()
    t.goto(-230, 30)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#9ACD32")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()

    t.penup()
    t.goto(-115, 30)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#32CD32")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()

    t.penup()
    t.goto(-90, 15)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#32CD32")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()

    t.penup()
    t.goto(-100, 10)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#9ACD32")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()


    t.penup()
    t.goto(-140, 10)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#32CD32")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()

    t.penup()
    t.goto(-140, 40)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#32CD32")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()

    t.penup()
    t.goto(-140, -20)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#32CD32")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()

    t.penup()
    t.goto(-120, -20)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#9ACD32")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()

    t.penup()
    t.goto(-200, 10)
    t.pendown()

    for _ in range(10):
        t.fillcolor("#32CD32")
        t.begin_fill()
        t.right(45)
        t.circle(10)
        t.end_fill()

    # desenhar o caminho
    t.color("black")
    t.penup()
    t.goto(-150, -400)
    t.pendown()

    for _ in range(10):
        t.circle(10, 90)
        t.circle(-10, 90)
    
    t.penup()
    t.goto(-50, -400)
    t.pendown()

    for _ in range(10):
        t.circle(10, 90)
        t.circle(-10, 90)

    t.hideturtle()
    turtle.done()

main()
