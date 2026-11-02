def remover_duplicidade(lista):
    conjunto = set(lista)
    return list(conjunto)


resultado = remover_duplicidade([1,1,4,5,6,7,2,4])
print(resultado)
