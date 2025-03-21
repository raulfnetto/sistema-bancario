"""Apresentação"""

print("Bem-vindo(a) ao Banco Raulzil")
print("Agradecemos por usar nosso sistema bancário.\n")

"""Definição de funções"""


class Banco:
    def __init__(self):
        self.saldo = 0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R$ {valor:.2f}")
            print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("❌ Valor inválido para depósito!")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: -R$ {valor:.2f}")
            print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")
        elif valor > self.saldo:
            print("❌ Saldo insuficiente!")
        else:
            print("❌ Valor inválido para saque!")

    def mostrar_extrato(self):
        print("\n📜 Extrato Bancário:")
        if not self.extrato:
            print("Nenhuma movimentação registrada.")
        else:
            for transacao in self.extrato:
                print(transacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}")


# Criando a conta bancária
banco = Banco()

while True:
    print("\n===== MENU BANCÁRIO =====")
    print("1️⃣  Depositar")
    print("2️⃣  Sacar")
    print("3️⃣  Ver Extrato")
    print("4️⃣  Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            valor = float(input("Informe o valor do depósito: R$ "))
            banco.depositar(valor)

        case "2":
            valor = float(input("Informe o valor do saque: R$ "))
            banco.sacar(valor)

        case "3":
            banco.mostrar_extrato()

        case "4":
            print("✅ Saindo do sistema. Obrigado por usar nosso banco!")
            break

        case _:
            print
