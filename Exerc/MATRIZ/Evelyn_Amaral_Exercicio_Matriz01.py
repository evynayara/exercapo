'''Criar um algoritmo que leia os elementos de uma matriz inteira 5 x 5 e escreva os elementos da diagonal principal.
OBS: Para ler a matriz e imprimir a diagonal principal deve ser utilizado o comando FOR.'''
lin = 0
col = 0
mat = [[0]*5, [0]*5, [0]*5, [0]*5, [0]*5]

for lin in range(0,5,1): 
    for col in range(0,5,1):
        mat[lin][col] = int(input("Digite o número da posição "+str(lin)+" "+str(col)+": "))

for lin in range(0,5,1):
    for col in range(0,5,1):
        if lin == col:
            print("[", mat[lin][col], "]", end='')
        