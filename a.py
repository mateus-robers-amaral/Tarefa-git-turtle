import turtle

# Configuração inicial
t = turtle.Turtle()
t.speed(2)  # Define a velocidade da tartaruga

# Função para desenhar uma árvore com contorno preto
def draw_tree(x, y):
    t.penup()
    t.goto(x, y)  # Posiciona a tartaruga
    t.pendown()
    t.color("black")  # Define a cor do contorno
    t.pensize(3)  # Define a espessura do contorno
    t.circle(50)  # Desenha o tronco da árvore
    t.left(90)
    t.color("green")  # Define a cor das folhas
    t.begin_fill()  # Começa a preencher as folhas
    t.circle(50, 120)  # Desenha uma parte das folhas da árvore
    t.left(120)
    t.circle(50, 120)  # Desenha outra parte das folhas da árvore
    t.end_fill()  # Termina de preencher as folhas

# Desenhar a árvore
draw_tree(0, 0)

# Manter a janela aberta
turtle.done()
