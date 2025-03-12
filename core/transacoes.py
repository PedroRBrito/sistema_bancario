from datetime import datetime

def saque(banco_usuario, cpf_login):

    if banco_usuario[cpf_login]["Conta"]["Saldo"] == 0:
        print("Saldo insuficiente!")
        return banco_usuario, cpf_login

    if banco_usuario[cpf_login]["Conta"]["Quantidade de transações"] <= 0:
        print("Limite de transações atingido, tente novamente amanhã!")
        return banco_usuario, cpf_login
            

    elif banco_usuario[cpf_login]["Conta"]["Quantidade de saques"] <= 0:
        print("Limite de saques atingido, tente novamente amanhã!")
        return banco_usuario, cpf_login
            
        
    valor_saque = input("Digite o valor do saque: ").strip()
        
    try:
        valor_saque = float(valor_saque)

        if valor_saque > banco_usuario[cpf_login]["Conta"]["Saldo"]:
            print("Saldo insuficiente!")
            return banco_usuario, cpf_login
            

        elif valor_saque > 500:
            print("Limite de R$500 por saque!")
            return banco_usuario, cpf_login
            

        elif valor_saque < 0:
            print("Por favor, coloque valores válidos!")
            return banco_usuario, cpf_login
            

        else:
            banco_usuario[cpf_login]["Conta"]["Saldo"] -= valor_saque
            banco_usuario[cpf_login]["Conta"]["Quantidade de saques"] -= 1
            banco_usuario[cpf_login]["Conta"]["Quantidade de transações"] -=1
            banco_usuario[cpf_login]["Conta"]["Registro da data da transação"] = datetime.now()

            banco_usuario[cpf_login]["Conta"]["Extrato"].append(f"Saque: R${valor_saque:0.2f}......Data:{banco_usuario[cpf_login]['Conta']['Registro da data da transação'].strftime('%d/%m/%Y %H:%M')}")

            print(f"Voce acaba de sacar: R${valor_saque:0.2f}")
            print(f"Seu saldo atual é: R${banco_usuario[cpf_login]['Conta']['Saldo']:0.2f}")

    except ValueError:
        print("Por favor, digite um número válido!")
        return banco_usuario, cpf_login
        
    if banco_usuario[cpf_login]["Conta"]["Quantidade de transações"] == 0:
        banco_usuario[cpf_login]["Conta"]["Quantidade de saques"] = 0

    return banco_usuario, cpf_login

def deposito(banco_usuario, cpf_login):
        
    try:
        if banco_usuario[cpf_login]["Conta"]["Quantidade de transações"] <= 0:
            print("Limite de transações atingido, tente novamente amanhã!")
            return banco_usuario, cpf_login

        valor_deposito = float(input("Digite o valor do deposito: "))

        if valor_deposito < 0:
            print("Por favor, coloque valores válidos!")
            return banco_usuario, cpf_login

        else:
            banco_usuario[cpf_login]["Conta"]["Saldo"] += valor_deposito
            banco_usuario[cpf_login]["Conta"]["Quantidade de transações"] -=1

            banco_usuario[cpf_login]["Conta"]["Registro da data da transação"] = datetime.now()
            banco_usuario[cpf_login]["Conta"]["Extrato"].append(f"Deposito: R${valor_deposito:0.2f}......Data:{banco_usuario[cpf_login]['Conta']['Registro da data da transação'].strftime('%d/%m/%Y %H:%M')}")

            print(f"Você acaba de depositar: R${valor_deposito:0.2f}")
            print(f"Seu saldo atual é: R${banco_usuario[cpf_login]['Conta']['Saldo']:0.2F}")

    except ValueError:
        print("Por favor, digite um número válido!")
        return banco_usuario, cpf_login

    if banco_usuario[cpf_login]["Conta"]["Quantidade de transações"] == 0:
        banco_usuario[cpf_login]["Conta"]["Quantidade de saques"] = 0

    return banco_usuario, cpf_login