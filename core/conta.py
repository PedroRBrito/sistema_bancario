from datetime import datetime

banco_usuario = {}
AGENCIA = '0001'

def cadastro_usuario(banco_usuario):

    nome = input("Informe seu nome: ").strip()
    data_nascimento = input("Informe sua data de nascimento: ").strip()
    cpf = input("Informe seu CPF: ").strip()
    logradouro = input("Informe seu logradouro: ").strip()
    numero = input("Informe o numero da sua casa: ").strip()
    bairro = input("Informe seu bairro: ").strip()
    cidade_estado = input("Informe a sua cidade e a sigla de seu estado (exemplo:Brasília/DF): ").strip()

    banco_usuario[cpf] = {
        "Nome" : nome,
        "CPF" : cpf,
        "Conta" : {},
        "Data de nascimento" : data_nascimento,
        "Endereço" :
            [
                logradouro,
                numero,
                bairro,
                cidade_estado]
        }

    return banco_usuario


def cadastro_conta(banco_usuario, numero_conta):

    cpf_conta = input("Informe um cpf para vincular sua conta: ").strip()

    if cpf_conta in banco_usuario:

        banco_usuario[cpf_conta]["Conta"]= {
            "Agência" : AGENCIA,
            "Número da conta" : numero_conta,
            "Saldo" : 0,
            "Extrato" : [],
            "Quantidade de saques" : 3,
            "Quantidade de transações" : 10,
            "Registro da data da transação" : datetime.now()
            }
        numero_conta += 1

    return banco_usuario

