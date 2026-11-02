def invertendo_numero_matematicamente(numero):
    numero_invertido = 0
    while numero != 0:
        numero_invertido = numero_invertido * 10 + numero % 10
        numero //= 10 # numero = numero // 10
    print(numero_invertido)

invertendo_numero_matematicamente(1234)