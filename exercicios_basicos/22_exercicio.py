def exponenciar(base, expoente):
    numero = base
    for i in range(expoente -1):
        numero *=base
    return numero


resultado = exponenciar(2, 8)
print(f"O resultado é {resultado}")