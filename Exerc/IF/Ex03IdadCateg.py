nome = ""
ida = 0

nome = input("Digite o nome do nadador: ")
ida = int(input("Digite a idade do nadador: "))

if((ida>=5) and (ida<=7)):
    print(f"O nadador {nome}, tem {ida} anos e é Infantil A.")
else:
    if((ida>=8) and (ida<=11)):
        print(f"O nadador {nome}, tem {ida} anos e é Infantil B.")
    else:
        if((ida>=12) and (ida<=13)):
            print(f"O nadador {nome}, tem {ida} anos e é Juvenil A.")
        else:
            if((ida>=14) and (ida<=17)):
                print(f"O nadador {nome}, tem {ida} anos e é Juvenil B.")
            else:
                if(ida>=18):
                    print(f"O nadador {nome}, tem {ida} anos e é Adulto.")
                else:
                    print(f"O nadador {nome} não possuí uma categoria válida.")