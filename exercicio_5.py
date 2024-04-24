def separar_pares_impares(numeros):
    pares = []
    impares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

# Ler os 20 números inteiros
numeros = []
for i in range(20):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

# Separar os números pares e ímpares
pares, impares = separar_pares_impares(numeros)

# Imprimir os três vetores
print("Números digitados:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)
