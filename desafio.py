from abc import ABC, abstractmethod
import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)
        
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        
class Conta:
    def __init__(self, numero, cliente):
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0
        self._agencia = "0001"
        self._historico = Historico()
        
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        
        if valor > saldo:
            print("Operação falho! Você não tem saldo suficiente.")    
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        else:
            print("Operação falhou| O valor informado é inválido.")
        
        return False
    
    def despositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False
        
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] = "Saque"]
        )
        
        if valor > self.limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif numero_saques >= self.limite_saques:
            print("Operação falhor! Número máximo de saques excedido.")
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""
Agencia: {self.agencia}
C/C: {self.numero}
Titular: {self.cliente.nome}
"""

class Historico:
    def __init__(self):
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {"tipo": transacao.__class__.__name__,
             "valor": transacao.valor,
             "data": datetime.now().strftime("%d-%n-%Y %H:%M:%s"),}
        )
        
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self): pass
    
    @abstractmethod
    def registrar(self, conta): pass
    
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property    
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Depositar(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
               
def menu():
    menu = """\n
==================MENU==================
[d]  Depositar
[s]  Sacar
[e]  Extrato
[nc] Nova Conta
[lc] Listar Contas
[nu] Novo Usuáiro
[q]  Sair\n
=> """
    return input(menu)

def extrato(saldo, /, *, extrato):
    print("\n==================EXTRATO==================")
    print("Não foram realzado movimentações" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=============================================")   

def novo_usuario(usuarios):
    cpf = input("Informe o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Usuario e CPF já existe")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereco (logrador, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("\nUsuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    
    return usuario_filtrado[0] if usuario_filtrado else None

def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuario não encontrado, fluxo de criação de conta encerrado!")

def main():
    saldo = 0
    limite= 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    valor = 0
    usuarios = []
    contas = []

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
            extrato(saldo, extrato = extrato)
            
        elif opcao == "nu":
            novo_usuario(usuarios)
            
        elif opcao == "nc":
            numero_conta = len(contas) +1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                
        elif opcao == "lc":
            listar_contas(contas)
            
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            
main()