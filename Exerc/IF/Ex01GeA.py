tc = ""
ct = 0.0
pc = 0.0
vt = 0.0

tc = input("Digite o tipo do seu carro (G - gasolina ou A - álcool):")
ct = float(input("Digite a capacidade de litros do seu tanque: "))

if(tc.upper()=="G"):
    print(f"O tipo do seu carro é de gasolina.")
else:
    print(f"O tipo do seu carro é de álcool.")

pc = float(input("Digite o preço do litro do combustível: "))
vt = ct * pc

print(f"O valor para encher o seu tanque é de: {vt:,.2f} reais")