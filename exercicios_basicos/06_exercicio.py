def fatorial(numero):
    fatoracao = i = 1

    while i <= numero:
        fatoracao = fatoracao * i
        i += 1
    return fatoracao


resultado = fatorial(5)
print(f"O resutado da fatoração é {resultado}")