
sal = float(input("Digite o salário do funcionário: "))

if(sal<=500):
    bon = (sal*0.05)
else:
    if((sal>500) and (sal<=1200)):
        bon = (sal*0.12)

if(sal<=600):
    aux = 150
else:
    aux = 100

print(f"O salário final do funcionário é: {sal + bon + aux}")