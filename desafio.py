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
        print("Depósito")
        
        saldo = float(input("R$ "))

        if saldo<0 :
            print("O saldo não pode negativo.")
    
    elif opcao == "s":
        print("Sacar")
    
    elif opcao == "e":
        print("Extrato")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")