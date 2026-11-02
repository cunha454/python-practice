def mostrar_divisiveis_por_5(lista):
    for numero in lista:
        if numero % 5 == 0:
            print(numero)


mostrar_divisiveis_por_5([10, 47, 90, 45, 92])