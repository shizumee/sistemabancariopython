menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Qual o valor a ser depositado?: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Este valor não é aceito! Digite um valor válido")

    elif opcao == "2":
        valor = float(input("Qual valor deseja sacar?: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Verifique se você possui saldo para esta operação.")

        elif excedeu_limite:
            print("Parece que você excedeu o limite, tente novamente mais tarde.")

        elif excedeu_saques:
            print("Você excedeu o de saque diário configurado em seu APP, para alterar acesse a área de segurança.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Você informou um valor inválido, tente novamente.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")