import turtle
import colorsys

# Configuração inicial
t = turtle.Turtle()
t.color("black")
t.speed(10)  # Define a velocidade da tartaruga

# Desenhar o retângulo principal da casa
x_casa = -100
y_casa = -250  # Move a casa para baixo
largura_casa = 200
altura_casa = 200
t.penup()
t.goto(x_casa, y_casa)  # Posiciona a tartaruga
t.pendown()
t.color("yellow")  # Define a cor da linha
t.begin_fill()  # Começa a preencher a forma
for _ in range(4):
    t.forward(largura_casa)
    t.left(90)
t.end_fill()  # Termina de preencher a forma

# Desenhar o telhado
t.penup()
t.goto(x_casa, y_casa + altura_casa)
t.pendown()
t.color("red")
t.begin_fill()
t.goto(x_casa + largura_casa / 2, y_casa + altura_casa + 100)
t.goto(x_casa + largura_casa, y_casa + altura_casa)
t.goto(x_casa, y_casa + altura_casa)
t.end_fill()

# Desenhar a porta
t.penup()
t.goto(x_casa + largura_casa / 4, y_casa)  # Posiciona a tartaruga na posição da porta
t.pendown()
t.color("brown")
t.begin_fill()
for _ in range(2):
    t.forward(largura_casa / 4)
    t.left(90)
    t.forward(altura_casa / 2)
    t.left(90)
t.end_fill()

# Desenhar o chão verde
x_chao = -turtle.window_width() / 2
y_chao = y_casa - 150
largura_chao = turtle.window_width()
altura_chao = y_casa - y_chao  # Altura do chão é determinada pela diferença entre a posição da casa e a posição do chão
t.penup()
t.goto(x_chao, y_chao)  # Posiciona a tartaruga abaixo da casa
t.pendown()
t.color("green")  # Define a cor da linha
t.begin_fill()  # Começa a preencher a forma
for _ in range(2):
    t.forward(largura_chao)
    t.left(90)
    t.forward(altura_chao)
    t.left(90)
t.end_fill()  # Termina de preencher a forma

t.speed(15)
# Função para desenhar uma árvore
def draw_tree(x, y):
    t.penup()
    t.goto(x, y)  # Posiciona a tartaruga
    t.pendown()
    t.color("brown")  # Define a cor da linha para o tronco
    t.begin_fill()  # Começa a preencher a forma
    t.left(90)
    t.forward(50)  # Desenha o tronco da árvore
    t.right(90)
    t.left(90)
    
    t.color("green")  # Define a cor da linha para as folhas
    t.begin_fill()  # Começa a preencher a forma
    t.circle(50, 120)  # Desenha uma parte das folhas da árvore
    t.left(30) #90
    t.circle(50, 120)  # Desenha outra parte das folhas da árvore
    t.end_fill()  # Termina de preencher a forma
    t.right(30) #120
    
    t.color("green")  # Define a cor da linha para as folhas
    t.begin_fill()
    t.circle(50, 120)  # Desenha uma parte das folhas da árvore
    t.left(30)
    t.circle(50, 120)  # Desenha outra parte das folhas da árvore
    t.end_fill()  # Termina de preencher a forma
    t.right(30)

    t.color("green")  # Define a cor da linha para as folhas
    t.begin_fill()
    t.circle(50, 120)  # Desenha uma parte das folhas da árvore
    t.left(30)
    t.circle(50, 120)  # Desenha outra parte das folhas da árvore
    t.end_fill()  # Termina de preencher a forma
    t.right(30)
    
    t.hideturtle()
    t.end_fill()  # Termina de preencher a forma

# Desenhar a árvore ao lado da casa
x_arvore = x_casa + largura_casa + 150
y_arvore = y_casa 
draw_tree(x_arvore, y_arvore)

def draw_one_color_arc(x,y,r,pensize,color):
    turtle.up()
    turtle.goto(x+r,y)
    turtle.down()
    turtle.seth(90)
    turtle.pensize(pensize)
    turtle.pencolor(color)
    turtle.circle(r,180)


turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor('light blue')
turtle.title('Rainbow In Python Turtle')
turtle.setup(700,700)
num_colors = 49

radius = 500
penwidth = 20*7/num_colors
hue = 0

for i in range(num_colors):
    (r,g,b) = colorsys.hsv_to_rgb(hue,1,1)
    draw_one_color_arc(0,-100,radius,penwidth,(r,g,b))
    radius -= (penwidth-1)
    hue += 0.9/num_colors

# Esconder a tartaruga
t.hideturtle()

# Manter a janela aberta
turtle.done()
