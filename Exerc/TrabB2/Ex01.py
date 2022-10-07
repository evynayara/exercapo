i = 0
j = 0
mat1 = [[0]*3, [0]*3, [0]*3]
mat2 = [[0]*5, [0]*5, [0]*5]
ra = 0
cpf = 0
cod = 0


for j in range(0,3,1):
    mat1[i][j] = int(input(f"Informe o RA do aluno {j+1}: "))
    mat1[i][j] = int(input(f"Informe o CPF do aluno {j+1}: "))
    mat1[i][j] = int(input(f"Informe o CÓDIGO do aluno {j+1}: "))
    mat2[i][j] = int(input(f"Informe a P1 do aluno {j+1}: "))
    mat2[i][j] = int(input(f"Informe a P2 do aluno {j+1}: "))
    mat2[i][j] = int(input(f"Informe a P3 do aluno {j+1}: "))
    mat2[i][j] = int(input(f"Informe a P4 do aluno {j+1}: "))
    mat2[i][j] = mat1[i][2] 