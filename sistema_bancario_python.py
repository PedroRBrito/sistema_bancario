
import datetime

SALDO_CONTA = 1000
saque = 0
deposito = 0
extrato = []
quantidade_saques = 3
ultimo_saque = None


while True:

    menu = f"""
-------------Menu--------------
Saldo : {SALDO_CONTA:0.2f}
Saques restantes: {quantidade_saques}
                                  
[S] Saque                         |
[D] Depósito                      |
[E] Extrato                       |
[F] Finalizar                     |
-------------------------------

"""
    
    opcao = input(menu)

    if ultimo_saque and ultimo_saque.date() != datetime.datetime.now().date():
        quantidade_saques = 3

    if opcao in ("s", "S"):
        
        if quantidade_saques <= 0:
            if ultimo_saque:
                tempo_passado = datetime.datetime.now() - ultimo_saque
                if tempo_passado.days == 0:
                    horas_restantes = 24 - tempo_passado.seconds // 3600
                    print(f"Limite diário de saques atingido. Tente novamente em {horas_restantes} horas.")
                    continue
                
                    
        saque = float(input("Digite o valor do saque: "))

        if saque > SALDO_CONTA:
            print("Saldo insuficiente!")

        elif saque > 500:
            print("Limite de R$500 por saque!")

        elif saque < 0:
            print("Por favor, coloque valores positivos")
        
        else:
            SALDO_CONTA -= saque
            quantidade_saques -= 1
            ultimo_saque = datetime.datetime.now()

            extrato.append(f"Saque: R${saque:0.2f}")

            print(f"Voce acaba de sacar: R${saque:0.2f}")
            print(f"Seu saldo atual é: R${SALDO_CONTA:0.2F}")
        

    elif opcao in ("d", "D"):

        deposito = float(input("Digite o valor do deposito: "))

        if deposito < 0:
            print("Por favor, coloque valores positivos")

        else:
            SALDO_CONTA += deposito

            extrato.append(f"Deposito: R${deposito:0.2f}")

            print(f"Você acaba de depositar: R${deposito:0.2f}")
            print(f"Seu saldo atual é: R${SALDO_CONTA:0.2F}")

        

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
        print("operação invalida")
