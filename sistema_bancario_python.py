
from datetime import datetime
from interface.menu import menu_conta, login, encerrar, menu_inicial, listar_contas
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
            'Agência': '0001',
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
            'Agência': '0001',
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
            'Agência': '0001',
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

    menu_saudacoes = menu_inicial()

    if menu_saudacoes in ("L", "l"):
        cpf_login = login()
    elif menu_saudacoes in ("C", "c"):
        listar_contas(banco_usuario)
        continue
    elif menu_saudacoes in ("s", "S"):
        break
    else:
        print("Opção inválida!")
        continue

    if cpf_login in banco_usuario:
            
            while True:

                opcao = menu_conta(banco_usuario, cpf_login)

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
    elif sair == ("s" or "S"):
        break
    else:
        print("Opção inválida!")