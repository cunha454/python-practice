def soma_do_raio(numero):
    numero_passado = 0
    print("Mostrando o número atual, o passado e a soma deles em um raio de", numero)

    for i in range(numero):
        print("N° atual:", i, "| N° passado:", numero_passado, "| Soma:", i + numero_passado)
        numero_passado = i

soma_do_raio(10)