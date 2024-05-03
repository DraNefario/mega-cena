import random

idades = [12,33,44,54]
idades.append(6)
idades[2] = 10
print(idades)

print(idades[4])

nomes = ["bob", "gabriel", "aliane"]
nomeAleatorio = random.choice(nomes)
print(nomeAleatorio)


contador = 0
while contador < len(idades):
    print(idades[contador]*2)
    contador += 1

i = 0    
print(idades[i]+idades[i+1], idades[i+2]-idades[i+3])
