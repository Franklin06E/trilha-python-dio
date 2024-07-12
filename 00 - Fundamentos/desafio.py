import datetime
import pytz

horario_operacao = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))
horario_formatado = horario_operacao.strftime("%d/%m/%Y %H:%M:%S")

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
valor = 0
while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input(f"Digite o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            print(f"Depósito efetuado no valor de R$ {valor:.2f}\n{horario_formatado}\n")
            extrato += f"Depósito: R$ {valor:.2f} {horario_formatado}\n"
            
        else: 
            print("Valor inválido.")
        
    elif opcao == "2":
        valor = float(input(f"Digite o valor a ser sacado: "))
        
        if valor > saldo:
            print("Saldo insuficiente.")

        elif valor > limite:
            print("Valor acima do limite permitido.")

        elif numero_saques == LIMITE_SAQUES:
            print("Número máximo de saques diários atingido.")

        elif saldo > 0:
            saldo -= valor
            print (f"Saque de R$ {valor:.2f} realizado.\n{horario_formatado}\n")
            extrato += f"Saque: R$ {valor:.2f} {horario_formatado}\n"
            numero_saques += 1

    elif opcao == "3":
        print("              EXTRATO               \n")
        print(f"Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "0":
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")
