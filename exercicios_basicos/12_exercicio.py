def inicio_igual_ao_final(lista):
    if lista[0] == lista[-1]:
        return True
    return False


print(f"O resultado é: {inicio_igual_ao_final([10,120,45,15])}")