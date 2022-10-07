ts = 0

ts = int(input("Digite a quantidade de pontos de água presentes no solo: "))

if(ts<=10):
    print("O tipo do solo é rochoso. ")
else:
    if((ts>10) and (ts<=40)):
        print("O tipo do solo é firme. ")
    else:
        if((ts>40) and (ts<=80)):
            print("O tipo do solo é pantanoso. ")
        else: 
            print("A quantidade é inválida.")