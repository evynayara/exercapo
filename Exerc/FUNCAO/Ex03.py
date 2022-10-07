n1 = 0 
n2 = 0
result = 0

def somar_numeros(numero1, numero2):  #com parâmetros
    result = numero1 + numero2
    return result                      #com return

n1 = int(input("Digite o valor do número 1: "))
n2 = int(input("Digite o valor do número 2: "))
print(f"A soma dos números é: {somar_numeros(n1,n2)}")  #chamando o return