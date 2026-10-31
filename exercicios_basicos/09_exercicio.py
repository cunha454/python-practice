def contador_de_vogais(palavra):
    vogais = "aeiou"
    quantidade = 0

    for letra in palavra.lower():
        if letra in vogais:
            quantidade +=1

    return quantidade


resutado = contador_de_vogais("Radiologia")
print("Quantidade de vogais:", resutado)
