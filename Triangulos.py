import turtle


def triangulo(x, y):
    # Irá levantar a caneta para não marcar o caminho que passar
    caneta.penup()

    # Irá mover o objeto até a posição x,y
    caneta.goto(x, y)

    # Irá abaixar a caneta
    caneta.pendown()

    # Construindo o triangulo
    for i in range(3):
        caneta.forward(100)
        caneta.left(120)
        caneta.forward(100)


# Função para pegar a tela
tela = turtle.Screen()

# Define o objeto
caneta = turtle.Turtle()

# Ao clicarem na tela ele chamará a função triangulo
turtle.onscreenclick(triangulo, 1)

turtle.listen()

turtle.done()
