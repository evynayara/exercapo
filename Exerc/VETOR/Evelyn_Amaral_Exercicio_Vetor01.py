cont = 0
vet = [0]*10

for cont in range(0,10,1):
    vet[cont] = int(input("Informe os 10 números: "))

print("Lista invertida: ")
print(vet[::-1])