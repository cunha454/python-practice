def piramide(numero_inicial, numero_final):
    for numero in range(numero_inicial, numero_final):
        for i in range(numero):
            print(numero, end="")
        print()
    

piramide(1,7)