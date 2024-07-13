import datetime

import pytz


def current_time():
    return datetime.datetime.now(pytz.timezone("America/Sao_Paulo")).strftime("%d/%m/%Y %H:%M:%S")

def deposito(saldo, valor, extrato):
    if valor <= 0:
        print("Valor de depósito inválido.")
        return saldo, extrato

    saldo += valor
    extrato += f"Depósito: R${valor:.2f}, realizado em {current_time()}\n"
    print(f"Depósito realizado no valor de R$ {valor:.2f}\n")
    return saldo, extrato

def saque(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        print("Valor de saque inválido.")
        return saldo, extrato, numero_saques

    if saldo < valor:
        print("Saldo insuficiente.\n")
        return saldo, extrato, numero_saques

    if valor > limite:
        print("Valor está acima do limite.\n")
        return saldo, extrato, numero_saques

    if numero_saques >= limite_saques:
        print("Limite de Saques Diários atingido.\n")
        return saldo, extrato, numero_saques

    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}, realizado em {current_time()}\n"
    print(f"Saque no valor de R$ {valor:.2f} realizado com sucesso.\n")
    return saldo, extrato, numero_saques + 1

def extrato_atual(saldo, extrato):
    print("----------EXTRATO----------")
    print("Não foram realizadas movimentações\n" if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("---------------------------")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF sem pontuações: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Este CPF já possui cadastro, operação inválida.")
        return

    nome = input("Digite o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço (logradouro, CEP - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco, "cpf": cpf})
    return usuarios

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }
    print("\nUsuário não encontrado, Criação de conta rejeitada!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):
    print("=== LISTA DE CONTAS ===")
    for conta in contas:
        print("=" * 50)
        print(f"Agência: {conta['agencia']}")
        print(f"Número da Conta: {conta['numero_conta']}")
        print(f"Titular: {conta['usuario']['nome']}")
    print("=" * 50)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    menu = """
    ================ MENU ================
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo usuário
    [5] Nova Conta
    [6] Listar Contas
    [0] Sair
    => """

    while True:
        opcao = input(menu)

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = saque(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == "3":
            extrato_atual(saldo, extrato = extrato)

        elif opcao == "4":
            criar_usuario(usuarios)
            print("Função não implementada ainda.")

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
