def achando_o_valor_maximo_e_o_minimo(numeros):
    return max(numeros), min(numeros)


resultado = achando_o_valor_maximo_e_o_minimo([12, 41, 1, -41, 144])
print(f"O menor valor é {resultado[1]} e maior é {resultado[0]}")