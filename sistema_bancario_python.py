
from datetime import datetime

SALDO_CONTA = 1000
saque = 0
deposito = 0
extrato = []
quantidade_saques = 3
quantidade_transacoes = 10
data_transacao = datetime.now()



while True:

    menu = f"""
----------Informações----------
Saldo : {SALDO_CONTA:0.2f}
Saques restantes: {quantidade_saques}
Transações Restantes: {quantidade_transacoes}
-------------Menu--------------                                  
[S] Saque                         |
[D] Depósito                      |
[E] Extrato                       |
[F] Finalizar                     |
-------------------------------

"""
    
    opcao = input(menu)

    if data_transacao.day < datetime.now().day:
        if quantidade_saques <= 0 or quantidade_transacoes <= 0:
            quantidade_saques = 3
            quantidade_transacoes = 10
            data_transacao = datetime.now()

    if opcao in ("s", "S"):
        
        if quantidade_transacoes <= 0:
            print("Limite de transações atingido, tente novamente amanhã!")
            continue

        elif quantidade_saques <= 0:
            print("Limite de saques atingido, tente novamente amanhã!")
            continue
        
        saque = input("Digite o valor do saque: ")
        
        try:
            saque = float(saque)

            if saque > SALDO_CONTA:
                print("Saldo insuficiente!")
                continue

            elif saque > 500:
                print("Limite de R$500 por saque!")
                continue

            elif saque < 0:
                print("Por favor, coloque valores válidos!")
                continue

            else:
                SALDO_CONTA -= saque
                quantidade_saques -= 1
                quantidade_transacoes -=1
                data_transacao = datetime.now()

                extrato.append(f"Saque: R${saque:0.2f}......Data:{data_transacao.strftime('%d/%m/%Y %H:%M')}")

                print(f"Voce acaba de sacar: R${saque:0.2f}")
                print(f"Seu saldo atual é: R${SALDO_CONTA:0.2f}")

        except ValueError:
            print("Por favor, digite um número válido!")
        
        if quantidade_transacoes == 0:
            quantidade_saques = 0
        

    elif opcao in ("d", "D"):

        try:
            if quantidade_transacoes <= 0:
                print("Limite de transações atingido, tente novamente amanhã!")
                continue

            deposito = float(input("Digite o valor do deposito: "))

            if deposito < 0:
                print("Por favor, coloque valores válidos!")

            else:
                SALDO_CONTA += deposito
                quantidade_transacoes -=1

                data_transacao = datetime.now()
                extrato.append(f"Deposito: R${deposito:0.2f}......Data:{data_transacao.strftime('%d/%m/%Y %H:%M')}")

                print(f"Você acaba de depositar: R${deposito:0.2f}")
                print(f"Seu saldo atual é: R${SALDO_CONTA:0.2F}")
        except ValueError:
            print("Por favor, digite um número válido!")

        if quantidade_transacoes == 0:
            quantidade_saques = 0

        

    elif opcao in ("e", "E"):
        print("-------------Extrato-----------")
        if not extrato:
            print("Sem histórico disponível!")
        else:
            for e in extrato:
                print(e)

    elif opcao in ("f", "F"):
        break

    else:
        print("Operação inválida!")
