'''
Faça um algoritmo que leia 50 valores reais e armazene em um vetor.
Modifique o vetor de modo que os valores das posições ímpares sejam aumentados em 5%, e os das posições pares sejam aumentados em 2%.
 Imprima depois o vetor resultante.
OBS: Para saber se um número é par você pode estar usando o comando %. Ex:  10 % 2, essa linha de comando retorna o resto da divisão do 
número 10 por 2, caso o resto da divisão for igual a zero, o número é par.'''

cont = 0.0
vet = [0.0]*5

for cont in range(0,5,1):
    vet[cont] = float(input("Digite o número da posição: "+str(cont)+ ": "))

    if cont%2==0: 
        vet[cont] = vet[cont]*1.02
    else:
        vet[cont] = vet[cont]*1.05

for cont in range(0,5,1):
    print(vet[cont], end='')
    print()