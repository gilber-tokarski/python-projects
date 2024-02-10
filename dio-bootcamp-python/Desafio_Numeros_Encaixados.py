try:
    N = int(input())

    while N > 0:
        valor_A = 0
        valor_B = 0

        print("Entre com o primeiro valor: ")
        try:
            valor_A = int(input())
            if valor_A == 0:
                print("Valor de A não pode ser 0!")
                break
        except ValueError:
            print("Valor inválido para A!")
            break

        print("Entre com o segundo valor: ")
        try:
            valor_B = int(input())
            if valor_B == 0:
                print("Valor de B não pode ser 0!")
                break
        except ValueError:
            print("Valor inválido para B!")
            break

        valor_A_str = str(valor_A)
        valor_B_str = str(valor_B)

        if len(valor_A_str) > 1000:
            print(f"Quantidade inválida. Tam. de A: {len(valor_A_str)} dígitos.")
            break
        if len(valor_B_str) > 1000:
            print(f"Quantidade inválida. Tam. de B: {len(valor_B_str)} dígitos.")
            break

        if valor_A_str.endswith(valor_B_str):
            print(f"Encaixa: {valor_A} e {valor_B}\n")
        else:
            print(f"Não encaixa: {valor_A} e {valor_B}\n")

        N -= 1
    else:
        print("Fim do while")

except ValueError:
    print("Você não digitou um número!")
