def multiplicacao_ou_soma(numero01, numero02):
    multiplicacao = numero01 * numero02

    if  multiplicacao <= 1000:
        return multiplicacao
    else:
        return numero01 + numero02


resultado = multiplicacao_ou_soma(30,50)
print("Resultado:", resultado)

resultado = multiplicacao_ou_soma(10,7)
print("Resultado:", resultado)