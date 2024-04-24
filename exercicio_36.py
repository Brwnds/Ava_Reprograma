def tabuada(numero, inicio, fim):
    print(f"Vou montar a tabuada de {numero} começando em {inicio} e terminando em {fim}:")
    for i in range(inicio, fim + 1):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")

# Solicitar input do usuário
numero = int(input("Montar a tabuada de: "))
inicio = int(input("Começar por: "))
fim = int(input("Terminar em: "))

# Chamada da função para imprimir a tabuada
tabuada(numero, inicio, fim)
