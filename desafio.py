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

def depositar(saldo, valor, extrato, /):
    if valor > 0 :
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print("\nDeposito realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é invalido.")

    return saldo, extrato

def sacar(* ,saldo, valor, extrato, limite, numero_saques, limite_saques):
    exceder_saldo = valor > saldo
    exceder_limite = valor > limite
    exceder_saque = numero_saques > limite_saques
    
    if exceder_saldo:
        print("Operação falho! Você não tem saldo suficiente.")
    elif exceder_limite:
        print("Operação falho! O valor do saque excedeu o limite.")
    elif exceder_saque:
        print("Operação falho! Número máximo de saques excedida.")
    elif valor > 0:
        saldo += valor
        extrato += f"Saque: R$ {valor:.2f}"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou| O valor informado é inválido.")
    
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
            
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Saque\nR$ "))
            
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )
    
        elif opcao == "e":
            print("Extrato: ")
            print(f"{extrato} \nSaldo final: R${saldo:.2f}")
    
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            
main()