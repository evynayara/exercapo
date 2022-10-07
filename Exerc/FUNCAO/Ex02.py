n1 = 0
n2 = 0
result = 0

def somar_numeros (numero1, numero2):    #função com parâmetros
    result = numero1 + numero2
    print(f"A soma dos dois números é: {result}")  #mas sem result, para imprimir o resultado na tela usa o print

n1 = int(input("Digite o valor do número 1: "))
n2 = int(input("Digite o valor do número 2: "))
somar_numeros(n1,n2)  #parametros é recomendado colocar os nomes da variavel diferente