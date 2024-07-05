def menu():
    menu = """\n
==================MENU==================
[d]  Depositar
[s]  Sacar
[e]  Extrato
[lc] Listar Contas
[nu] Novo Usuáiro
[q]  Sair\n
=> """
    return input(menu)

def depositar(saldo, valor, extrato):
    if valor > 0 :
        saldo += valor
        extrato += f"Deposito: R${valor:.2f}\n"
    else:
        print("\nOperação falhou! O valor informado é invalido.")

    return saldo, extrato

def main():
    saldo = 0
    limite= 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    valor = 0

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Depósito\nR$ "))
            
            saldo , extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            sacar = float(input("Sacar\nR$ "))

            if numero_saques < LIMITE_SAQUES:
                if saldo >= 0 and saldo >= sacar:
                    if sacar > 0 and sacar <= limite:
                        saldo -= sacar
                        numero_saques+=1

                        extrato += f"Saque: R${sacar:.2f}\n"
                    else:
                        print("Não pode sacar 0 ou maior que 500 reais.")
                else:
                    print("Não pode sacar")
            else:
                print("O numero de saques não pode ser maior que 3")
    
        elif opcao == "e":
            print("Extrato: ")
            print(f"{extrato} \nSaldo final: R${saldo:.2f}")
    
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            
main()