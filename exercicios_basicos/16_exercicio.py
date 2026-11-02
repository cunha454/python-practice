def verificar_palindromo(numero):
    numero_str = str(numero)
    numero_invertido = numero_str[::-1]
    if numero_str == numero_invertido:
        print("Palíndromo!!!")
    else:
        print("Não Palíndromo")


verificar_palindromo(1221)