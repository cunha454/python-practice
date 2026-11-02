import pyperclip as pyc


def gerador(numero_inicial, numero_final):
    i, texto = 0, ""
    for exercicio in range(numero_inicial, numero_final + 1):
        numero = numero_inicial + i
        texto +=(f"{numero}. **[Execício {numero}]({numero}_exercicio.py)** → \n\n")
        i +=1
        pyc.copy(texto)
    print("O texto foi copiado com sucesso!!!")


gerador(int(input("Digite o início: ")), int(input("Digite o fim: ")))
