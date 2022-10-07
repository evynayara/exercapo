nome = ""
sit = ""
n1 = 0.0
n2 = 0.0
med = 0.0

nome = input("Digite o nome do aluno: ")
n1 = float(input("Digite a nota 1 do aluno: "))
n2 = float(input("Digite a nota 2 do aluno: "))

med = (n1 + n2)/2

if(med >= 6):
    sit = "Aprovado"
else:
    if(med >= 4 ) and (med < 6):
        sit = "Recuperação"
    else: 
        sit = "Reprovado"
print(f"{nome}, a sua média é: {med}, e você está: {sit}")