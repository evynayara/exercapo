cont = 0
vet = [0]*5

for cont in range(0,5,1):
    vet[cont] = int(input("Informe o número para a posição "+ str(cont) + ": "))

for cont in range(0,5,1):
    print(vet[cont], end='')