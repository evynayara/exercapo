smin = 0.0
ht = 0
dep = 0
qhe = 0

smin = float(input("Digite o valor do salário mínimo: "))
ht = int(input("Digite o número de horas inteiras trabalhadas: "))
dep = int(input("Digite o número de dependentes que o trabalhador possui: "))
qhe = int(input("Digite a quantidade de horas extras inteiras trabalhadas: "))

vht = smin/5
smes = ht * vht
tdep = dep*32
vhe = qhe*(vht*1.5)
sbru = smes + tdep + vhe

if((sbru>=200) and (sbru<=500)):
    imp = (sbru*0.1)
else:
    if(sbru>500):
        imp = (sbru*0.2)
    else:
        imp = 0
sliq = sbru - imp

if(sliq<=350):
    grt = 100
else: 
    grt = 50

sfin = sliq + grt

print(f"O salário final do funcionário é: {sfin:,.2f}")