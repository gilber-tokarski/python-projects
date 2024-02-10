menu = """
*** S I S T E M A  B A N C Á R I O ***
Escolha sua opção:
[1] Depósito
[2] Saque
[3] Extrato
[9] Sair
=> """

saldo = 0
quantidade_saques = 0
limite = 500.00
LIMITE_SAQUES = 3
extrato = "-------> E X T R A T O <-------\n"

while True:
    opcao = input(menu)

    if opcao == "1":
        deposito = input("Informe o valor para depósito => ").replace(",", "X").replace(".", ",").replace("X", ".")
        deposito = round(float(deposito), 2)
        if deposito <= 0:
            print("Valor de depósito inválido! Refaça a operação.")
        else:
            saldo = round(saldo + deposito, 2)
            extrato = extrato + f"-> Depósito: R$ {deposito:.2f}(+)\n"

    elif opcao == "2":
        if saldo == 0:
            print("Saldo zerado para esta operação!")
            continue

        print(f"Saldo atual => R$ {saldo:.2f}(+)")

        saque = input("Informe o valor para saque => ").replace(",", "X").replace(".", ",").replace("X", ".")
        saque = round(float(saque), 2)

        if saque <= 0:
            print("Valor de saque inválido! Refaça a operação.")
        elif quantidade_saques >= LIMITE_SAQUES:
            print("Quantidade de saques diária excedida! Tente novamente amanhã.")
        elif saque > limite:
            print("Limite de saque de R$500,00 excedido! Refaça a operação.")
        elif saque > saldo:
            print("Saldo insuficiente para concluir o saque! Refaça a operação.")
        else:
            quantidade_saques = quantidade_saques + 1
            saldo = round(saldo - saque, 2)
            extrato = extrato + f"-> Saque: R$ {saque:.2f}(-)\n"

    elif opcao == "3":
        print(extrato)
        print(f"--> SALDO ATUAL => R$ {saldo:.2f} <--")

    elif opcao == "9":
        print("----> A T É  L O G O!!! <----")
        break

    else:
        print("Operação inválida!")
