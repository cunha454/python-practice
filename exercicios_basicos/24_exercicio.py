def fibonacci(tamanho):
    sequencia = [0, 1]

    if tamanho <= 0:
        return "Erro"
    elif tamanho == 1:
        return [0]
    else:
        for i in range(tamanho - 2):
            numero_atual = sequencia[-1] + sequencia[-2]
            sequencia.append(numero_atual)

        return sequencia


resultado = fibonacci(2)
print(resultado)