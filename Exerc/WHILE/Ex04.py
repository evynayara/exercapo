resp = 0.0
c9 = 0.0
c12 = 0.0
c23 = 0.0
c40 = 0.0
co = 0.0
vt = 0.0

resp = float(input("Digite o número do canal: "))

while resp != 0:
    resp = float(input("Digite o número do canal: "))
    vt += 1
    if resp == 9:
        c9 = c9 +1
    else: 
        if resp == 12:
            c12 = c12 
        else:
            if resp == 23:
                c23 += 1
            else:
                if resp == 40:
                    c40 += 1
                else:
                    co +=1
                    
c9 = c9*100/vt
c12 = c12*100/vt
c23 = c23*100/vt
c40 = c40*100/vt
co = co*100/vt

print(f"A porcentagem de audiência da emissora do canal 9 é de: {c9}")
print(f"A porcentagem de audiência da emissora do canal 12 é de: {c12}")
print(f"A porcentagem de audiência da emissora do canal 23 é de: {c23}")
print(f"A porcentagem de audiência da emissora do canal 40 é de: {c40}")
print(f"A porcentagem de audiência dos outros canais é de: {co}")
