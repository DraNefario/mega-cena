import random

numMEGA = [30, 49, 48, 43, 23, 78, 44, 4, 43, 123, 12, 56, 98]

sorteados = random.sample(numMEGA, 6)

escolhidos = [0] * 6  
contador = 0
print(numMEGA)

while contador < len(escolhidos):
    escolha = int(input("Escolha um número de numMEGA: "))
    if escolha in numMEGA:
        escolhidos[contador] = escolha
        contador += 1
    else:
        print("Número não está na lista numMEGA. Escolha novamente.")

acertos = 0
i = 0
while i < len(escolhidos):
    if escolhidos[i] in sorteados:
        acertos += 1
    i += 1

print("Números sorteados:", sorteados)
print("Números escolhidos:", escolhidos)
print("Números de acertos:", acertos)