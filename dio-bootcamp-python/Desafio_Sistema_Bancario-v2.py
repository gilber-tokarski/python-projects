import textwrap


def menu():
    menu = """
    *** S I S T E M A  B A N C Á R I O ***
    Escolha sua opção:
    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Criar conta
    [5] Listar contas
    [6] Criar usuário
    [9] Sair
    => """
    return input(textwrap.dedent(menu))


def depositar(p_saldo, p_extrato, /):
    deposito = input("Informe o valor para depósito => ").replace(",", "X").replace(".", ",").replace("X", ".")
    deposito = round(float(deposito), 2)
    if deposito <= 0:
        print("Valor de depósito inválido! Refaça a operação.")
    else:
        p_saldo = round(p_saldo + deposito, 2)
        p_extrato = p_extrato + f"-> Depósito: R$ {deposito:.2f}(+)\n"
    return p_saldo, p_extrato


def sacar(*, p_saldo, p_quantidade_saques, p_limite, p_limite_saques, p_extrato):
    if p_saldo == 0:
        print("Saldo zerado para esta operação!")
        return p_saldo, p_quantidade_saques, p_extrato

    print(f"Saldo atual => R$ {p_saldo:.2f}(+)")

    saque = input("Informe o valor para saque => ").replace(",", "X").replace(".", ",").replace("X", ".")
    saque = round(float(saque), 2)

    if saque <= 0:
        print("Valor de saque inválido! Refaça a operação.")
    elif p_quantidade_saques >= p_limite_saques:
        print("Quantidade de saques diária excedida! Tente novamente amanhã.")
    elif saque > p_limite:
        print("Limite de saque de R$500,00 excedido! Refaça a operação.")
    elif saque > p_saldo:
        print("Saldo insuficiente para concluir o saque! Refaça a operação.")
    else:
        p_quantidade_saques = p_quantidade_saques + 1
        p_saldo = round(p_saldo - saque, 2)
        p_extrato = p_extrato + f"-> Saque: R$ {saque:.2f}(-)\n"
    return p_saldo, p_quantidade_saques, p_extrato


def tirar_extrato(p_saldo, /, *, p_extrato):
    print(p_extrato)
    print(f"--> SALDO ATUAL => R$ {p_saldo:.2f} <--")


def criar_usuario(p_usuarios):
    cpf = input("CPF: ").replace(".", "").replace("-", "")
    usuario = pesquisar_usuario(cpf, p_usuarios)

    if usuario:
        print("Já existe um usuário com esse CPF!")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento [dd-mm-yyyy]: ")
    endereco = input("Endereço [logradouro, Número - Bairro - Cidade/Estado]: ")

    p_usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário cadastrado com sucesso.")


def pesquisar_usuario(p_cpf, p_usuarios):
    pesquisa = [usuario for usuario in p_usuarios if usuario["cpf"] == p_cpf]
    return pesquisa[0] if pesquisa else None


def criar_conta(p_agencia, p_numero_conta, p_usuarios):
    cpf = input("CPF do usuário: ")
    usuario = pesquisar_usuario(cpf, p_usuarios)
    if usuario:
        print("Conta criada!")
        return {"agencia": p_agencia, "numero_conta": p_numero_conta, "usuario": usuario}
    print("Usuário não encontrado! Refaça a operação.")


def listar_contas(p_contas):
    for conta in p_contas:
        linha = f"""
                Agência: {conta['agencia']}
                C/C: {conta['numero_conta']}
                Titular: {conta['usuario']['nome']}
        """
        print('=' * 50)
        print(textwrap.dedent(linha))


def main():
    saldo = 0
    quantidade_saques = 0
    limite = 500.00
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    extrato = "-------> E X T R A T O <-------\n"
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "2":
            saldo, quantidade_saques, extrato = sacar(p_saldo=saldo, p_quantidade_saques=quantidade_saques, p_limite=limite, p_limite_saques=LIMITE_SAQUES, p_extrato=extrato)
        elif opcao == "3":
            tirar_extrato(saldo, p_extrato=extrato)
        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "5":
            listar_contas(contas)
        elif opcao == "6":
            criar_usuario(usuarios)
        elif opcao == "9":
            print("----> A T É  L O G O!!! <----")
            break
        else:
            print("Operação inválida!")


main()
