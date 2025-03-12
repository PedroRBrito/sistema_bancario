
from datetime import datetime
from interface.menu import menu, login, encerrar
from core.transacoes import saque, deposito
from core.conta import cadastro_usuario, cadastro_conta
from repository.extrato import extrato
from services.regras_bancarias import data_transacao



numero_conta = 4
banco_usuario= {
    '12345678900': {
        'Nome': 'Carlos Silva',
        'CPF': '12345678900',
        'Conta': {
            'Número da conta': 1,
            'Saldo': 0,
            'Extrato': [],
            'Quantidade de saques': 3,
            'Quantidade de transações': 10,
            'Registro da data da transação': datetime(2025, 3, 12, 2, 29, 38, 464703)
            },
        'Data de nascimento': '01/01/1985',
        'Endereço': ['Rua A', '10', 'Centro', 'Brasília/DF']
    },
    '98765432100': {
        'Nome': 'Ana Oliveira',
        'CPF': '98765432100',
        'Conta': {
            'Número da conta': 2,
            'Saldo': 0,
            'Extrato': [],
            'Quantidade de saques': 3,
            'Quantidade de transações': 10,
            'Registro da data da transação': datetime(2025, 3, 12, 2, 29, 38, 464774)
            },
        'Data de nascimento': '15/06/1992',
        'Endereço': ['Rua B', '20', 'Sul', 'São Paulo/SP']
    },
    '11122334455': {
        'Nome': 'Luís Costa',
        'CPF': '11122334455',
        'Conta': {
            'Número da conta': 3,
            'Saldo': 0,
            'Extrato': [],
            'Quantidade de saques': 3,
            'Quantidade de transações': 10,
            'Registro da data da transação': datetime(2025, 3, 12, 2, 29, 38, 464838)
        },
        'Data de nascimento': '10/03/1978',
        'Endereço': ['Rua C', '30', 'Norte', 'Rio de Janeiro/RJ']
    }
}

while True:

    cpf_login = login()

    if cpf_login in banco_usuario:
            
            while True:

                opcao = menu(banco_usuario, cpf_login)

                banco_usuario, cpf_login = data_transacao(banco_usuario, cpf_login)

                if opcao in ("s", "S"):
                    banco_usuario, cpf_login = saque(banco_usuario, cpf_login)
                    print(banco_usuario)

                elif opcao in ("d", "D"):
                    banco_usuario, cpf_login  = deposito(banco_usuario, cpf_login)
                    print(banco_usuario)

                elif opcao in ("e", "E"):
                    extrato(banco_usuario, cpf_login)
                    print(banco_usuario)

                elif opcao in ("t", "T"):
                    break

                else:
                    print("Operação inválida!")

    else:
        banco_usuario = cadastro_usuario(banco_usuario)
        banco_usuario = cadastro_conta(banco_usuario, numero_conta)
        numero_conta += 1
        print(banco_usuario)
        continue

    sair = encerrar()

    if sair == ("t" or "T"):
        continue
    else:
        break