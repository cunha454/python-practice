def lista_de_frutas(lista, nova_fruta):
    lista.pop(1)
    lista.append(nova_fruta)
    return lista


resultado = lista_de_frutas(["banana", "maca", "pera", "uva", "figo"], "coco")
print(f"A lista é {resultado}")