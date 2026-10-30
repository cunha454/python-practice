def mostrando_somente_indice_par(palavra):
    indices_pares = palavra[0::2] #[inico:fim:pulado]

    for letra in indices_pares:
        print(letra)


mostrando_somente_indice_par("python")