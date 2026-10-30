def trocando_valores(numero01, numero02):
    a = numero01
    b = numero02
    print(f"Antes  => A = {a}, B = {b}")

    a, b = b, a
    print(f"Depois => A = {a}, B = {b}")


trocando_valores(5,10)
