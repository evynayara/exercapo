notasAluno = []
dadosAluno = []
#adicionando os alunos 
def adicionaAluno(qtd):
    for i in range (qtd): 
        ra = int(input(f"Informe o R.A do aluno {i+1}:"))
        cpf = int(input(f"Informe o CPF do aluno {i+1}:"))
        cod = int(input(f"Informe o CÓDIGO do aluno {i+1}:"))
        notasAluno.append(adicionaNotas(cod))
        dadosAluno.append([ra, cpf, cod])
#adicionando as notas
def adicionaNotas(cod):
    notas = [cod]
    media = 0.0
    for i in range (4):
        nota = float(input(f"Informe a nota {i+1} do aluno:"))
        media = media + nota
        notas.append(nota)
    media = media/4
    notas.append(media)
    return notas
#verificando a situação do aluno
def verificaNotas(media):
    if(media>=6):
        print("Situação: Aprovado.")
    else:
        if(media>=4):
            print("Situação: Recuperação.")
        else:
            print("Situação: Reprovado.")
#consulta do usuário
def fazConsulta(cons):
    encontrou = False
    if(cons==1):
        resp = int(input("Informe o R.A do aluno: "))
        for i in range(0, len(dadosAluno), 1):
            if(dadosAluno[i][0]==resp):
                encontrou = True
                print(f"R.A do aluno: {dadosAluno[i][0]}")
                for j in range(0, len(notasAluno), 1):
                    if(notasAluno[j][0]==dadosAluno[i][2]):
                        for k in range(1,5,1): 
                            print(f"Nota {k}: {notasAluno[j][k]} \t", end='')
                            if (k!=4):
                                print(f"|\t", end='')
                        print()
                        print(f"Média: {notasAluno[j][5]}")
                        verificaNotas(notasAluno[j][5])
    else: 
        if(cons==2):
            resp = int(input("Informe o CPF do aluno: "))
            for i in range(0, len(dadosAluno), 1):
                if(dadosAluno[i][1]==resp):
                    encontrou = True
                    print(f"CPF do aluno: {dadosAluno[i][1]}")
                    for j in range(0, len(notasAluno), 1):
                        if(notasAluno[j][0]==dadosAluno[i][2]):
                            for k in range(1,5,1): 
                                print(f"Nota {k}: {notasAluno[j][k]} \t", end='')
                                if (k!=4):
                                    print(f"|\t", end='')
                            print()
                            print(f"Média: {notasAluno[j][5]}")
                            verificaNotas(notasAluno[j][5])
        else: 
            if(cons==3):
                resp = int(input("Informe o CÓDIGO do aluno: "))
                for i in range(0, len(dadosAluno), 1):
                    if(dadosAluno[i][2]==resp):
                        encontrou = True
                        print(f"CÓDIGO do aluno: {dadosAluno[i][2]}")
                        for j in range(0, len(notasAluno), 1):
                            if(notasAluno[j][0]==dadosAluno[i][2]):
                                for k in range(1,5,1): 
                                    print(f"Nota {k}: {notasAluno[j][k]} \t", end='')
                                    if (k!=4):
                                        print(f"|\t", end='')
                                print()
                                print(f"Média: {notasAluno[j][5]}")
                                verificaNotas(notasAluno[j][5])
            if(not(encontrou)):
                print("Nenhum aluno foi encontrado!")

adicionaAluno(3)
continuar = True
while(continuar):
    print("Informe qual tipo de consulta deseja realizar.")
    print("1- R.A do aluno ")
    print("2- CPF do aluno")
    print("3- Código do aluno")
    opc  = int(input("Consulta: "))
    if(opc>=1 and opc <=3):
        fazConsulta(opc)
    else:
        print("Valor inválido.")
    cont = input("Deseja pesquisar outro aluno? (S/sim ou N/não): ")
    if(cont.upper()=="S"):
        continuar = True
    else:
        if(cont.upper()=="S"):
            continuar = False
        else:
            print("Valor inválido.")
            continuar = False