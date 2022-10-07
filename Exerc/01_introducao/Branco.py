'''
   == | != | < | > | <= | >= 
   and | or | not 

   var.upper() para converter a variavel para maiusculos
'''
nome = ""
i = 0
d = 0.0
soma = 0.0

nome = input("Digite o nome: ")
i = int(input("Digite o número inteiro: "))
d = float(input("Digite o valor decimal: "))

soma = i + d

print(f"{nome}, o valor da soma do número inteiro com o número decimal é de: {soma:,.2f} ")
