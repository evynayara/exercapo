num = 0
cont = 0


def num_maior(numero, maior):
    if(numero>maior):
        maior = numero
    return maior

def num_menor(numero, menor):
    if(numero<menor):
        menor = numero
    return menor
maior = 0
menor = 9999999999999999

for cont in range(0,5,1): 
    num = int(input("Digite o número: "))
    maior = num_maior(num, maior)
    menor = num_menor(num, menor)
    
print(f"O maior número digitado é: {maior}")
print(f"O menor número digitado é: {menor}")
