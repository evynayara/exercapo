mat = [[0]*3, [0]*3, [0]*3]

for i in range(0,3,1):
    for j in range(0,3,1):
        mat[i][j] = int(input(f"Informe o valor da posição {i+1}, {j+1}:"))

for i in range(0,3,1):
    for j in range(0,3,1):
        print(f"[ {mat[i][j]} ]", end='')
    print()