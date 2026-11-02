def unindo_listas_com_restricoes(lista01, lista02):
    lista_filha = []
    for numero in lista01:
        if numero % 2 == 1:
            lista_filha.append(numero)
    for numero in lista02:
        if numero % 2 == 0:
            lista_filha.append(numero)
    print(lista_filha)


unindo_listas_com_restricoes([10, 15, 32, 45], [14, 53, 75, 42])