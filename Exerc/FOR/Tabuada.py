cont = 0
num = 0

num = int(input("Digite o número para obter a tabuada: "))

for cont in range(1,11,1):
    print(f"{num} X {cont} = {num * cont}")