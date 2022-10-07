cont = 0
idad = 0 
soma = 0 
menor = 0
maior = 0

n = int(input("Digite o número de idades que você irá digitar: "))

for cont in range(0,n,1):
    idad = int(input(f"Digite a idade {cont+1}: "))

    if(cont == 0):
        maior = idad
        menor = idad
    else: 
        if(idad>maior):
            maior = idad
        if(idad<menor):
            menor = idad
    
    soma = soma + idad 
    media = soma/n

print(f"A média dos {cont+1} números digitados: {media}")
print(f"O maior número digitado: {maior}")
print(f"O menor número digitado: {menor}")