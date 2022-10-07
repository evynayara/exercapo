lin = 0
col = 0
mat = [[0]*3, [0]*3, [0]*3]

for lin in range(0,3,1):
    for col in range(0,3,1):
        mat[lin][col] = int(input("Informe o número para a posição: " + str(lin) + " " + str(col) + ": "))

for lin in range(0,3,1):
    for col in range(0,3,1):
        print("[", mat[lin][col],"]", end='')
    print()