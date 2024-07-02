menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=>"""

saldo = 0
limite= 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        saldo = float(input("Depósito\nR$ "))

        if saldo<0 :
            print("O saldo não pode negativo.")
    
    elif opcao == "s":
        sacar = float(input("Sacar\nR$ "))

        if numero_saques < LIMITE_SAQUES:
            if saldo >= 0 and saldo >= sacar:
                if sacar > 0 and sacar <= limite:
                    saldo -= sacar
                    numero_saques+=1
                else:
                    print("Não pode sacar 0 ou maior que 500 reais.")
            else:
                print("Não pode sacar")
        else:
            print("O numero de saques não pode ser maior que 3")
    
    elif opcao == "e":
        print("Extrato")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")