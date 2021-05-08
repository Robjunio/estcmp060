import turtle
import math


def fibonacci_plot(x):

    tamanho_a = 0
    tamanho_b = 1
    quadrado_a = tamanho_a
    quadrado_b = tamanho_b

    # Fazendo o primeiro quadrado.
    Tortuguita.forward(tamanho_b * factor)
    Tortuguita.left(90)
    Tortuguita.forward(tamanho_b * factor)
    Tortuguita.left(90)
    Tortuguita.forward(tamanho_b * factor)
    Tortuguita.left(90)
    Tortuguita.forward(tamanho_b * factor)

    # Sequência de Fibonacci
    temp = quadrado_b
    quadrado_b = quadrado_b + quadrado_a
    quadrado_a = temp

    # loop para desenhar os outros Quadrados.
    for i in range(1, n):
        Tortuguita.backward(quadrado_a*factor)
        Tortuguita.right(90)
        Tortuguita.forward(quadrado_b*factor)
        Tortuguita.left(90)
        Tortuguita.forward(quadrado_b*factor)
        Tortuguita.left(90)
        Tortuguita.forward(quadrado_b*factor)

        temp = quadrado_b
        quadrado_b = quadrado_b + quadrado_a
        quadrado_a = temp

    # Voltar a caneta para o ponto inicial.
    Tortuguita.penup()
    Tortuguita.setposition(factor, 0)
    Tortuguita.seth(0)
    Tortuguita.pendown()

    # Mudando a cor da caneta para vermelho.
    Tortuguita.pencolor("red")

    # O gráfico da espiral em si.
    Tortuguita.left(90)
    for i in range(x):
        print(tamanho_b)
        fdwd = math.pi * tamanho_b * factor/2
        fdwd /= 90
        for j in range(90):
            Tortuguita.forward(fdwd)
            Tortuguita.left(1)
        temp = tamanho_a
        tamanho_a = tamanho_b
        tamanho_b = temp + tamanho_b


Fator = int(input("Insira a escala do grafico (Deve ser >= 1):"))

n = int(input("Insira o numero de interações (Deve ser maior que 1): "))

if n > 1:
    Tortuguita = turtle.Turtle()  # Criando uma turtle, com o nome de Tortuguita.
    Tortuguita.speed(100)
    fibonacci_plot(n)
    turtle.done()
else:
    print("O numero deve ser maior que 1!")