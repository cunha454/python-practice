def verificar_palindromo_matematicamente(numero):
    numero_original = numero
    numero_invertido = 0

    while numero != 0:
        numero_invertido = numero_invertido * 10 + numero % 10
        numero = numero // 10

    if numero_original == numero_invertido:
        return True
    else:
        return False


resultado = verificar_palindromo_matematicamente(171)
print("O número é um palíndromo?:", resultado)