def piramede_invertida(tamanho):
    i = tamanho
    for camada in range(tamanho,0,-1):
        print("*" * camada)


piramede_invertida(5)