from datetime import datetime

def data_transacao(banco_usuario, cpf_login):
    if banco_usuario[cpf_login]["Conta"]["Registro da data da transação"].day < datetime.now().day and (banco_usuario[cpf_login]["Conta"]["Quantidade de saques"] <= 0 or banco_usuario[cpf_login]["Conta"]["Quantidade de transações"] <= 0):
        banco_usuario[cpf_login]["Conta"]["Registro da data da transação"] = datetime.now()
        banco_usuario[cpf_login]["Conta"]["Quantidade de saques"] = 3
        banco_usuario[cpf_login]["Conta"]["Quantidade de transações"] = 10

        return banco_usuario, cpf_login
    else:
        return banco_usuario, cpf_login