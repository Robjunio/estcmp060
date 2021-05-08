import turtle


def arvore_fractal(tam, niv):
    if niv > 0:
        # Define as cores
        turtle.colormode(255)

        arvore.pencolor(0, 255 // niv, 0)

        # Desenha a base da arvore
        arvore.forward(tam)
        arvore.rt(angulo)

        # Utiliza da recursividade para construir o lado direito da árvore
        arvore_fractal(0.8 * tam, niv-1)
        arvore.pencolor(0, 255//niv, 0)
        arvore.lt(2 * angulo)

        # Utiliza da recursividade para construir o lado esquerdo da árvore
        arvore_fractal(0.8 * tam, niv - 1)

        arvore.pencolor(0, 255 // niv, 0)

        arvore.rt(angulo)
        arvore.forward(-tam)


tamanho, niveis = input("Insira o tamanho da arvore, e a quantidade de niveis "
                        "(Separadas por um espaço, e lembre-se os valores "
                        "devem ser >0):").split()
tamanho = int(tamanho)
niveis = int(niveis)

if tamanho > 0 and niveis > 0:
    # Criando e definindo a velocidade e angulo da turtle chamada arvore.
    arvore = turtle.Turtle()
    arvore.speed("fastest")
    arvore.rt(-90)
    angulo = 30
    # Mostra a arvore com x de tamanho e y niveis.
    arvore_fractal(tamanho, niveis)
    turtle.done()
else:
    print("Os valores devem ser positivos e separador por apenas um espaço")
