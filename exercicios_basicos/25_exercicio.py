def ano_bissexto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        print("Ano Bissexto")
    else:
        print("Ano normal")


ano_bissexto(2000)