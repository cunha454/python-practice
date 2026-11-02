def tabuada(inicio, fim):
    for linha in range(inicio, fim):
        for unidade in range(inicio, fim):
            print(f"{unidade * linha}", end="\t")
        print()


tabuada(1, 11)

