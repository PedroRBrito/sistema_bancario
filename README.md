# Sistema Bancário Python

Este projeto implementa um **sistema bancário simples** utilizando Python. Ele permite o cadastro de usuários, criação de contas bancárias, realização de transações como **saques** e **depósitos**, além de possibilitar a consulta de **extratos** e **dados pessoais**.

## Funcionalidades

- **Cadastro de Usuário**: O sistema permite que o usuário se cadastre informando dados pessoais como nome, CPF, data de nascimento, e endereço.
  
- **Cadastro de Conta Bancária**: Após o cadastro do usuário, é possível criar uma conta bancária associada a um CPF com número de conta, saldo inicial, e limite de transações.

- **Operações Bancárias**:
  - **Saques**: O usuário pode realizar saques de sua conta, com limite de tentativas.
  - **Depósitos**: O sistema permite que o usuário deposite valores na conta.
  - **Extrato**: O usuário pode consultar o extrato de suas transações realizadas.

- **Controle de Transações**: Limites de saques e transações, além do registro da data e hora de cada transação.

## Tecnologias Utilizadas

- Python 3
- Biblioteca `datetime` para registro de transações

## Como Usar

1. Clone este repositório.
2. Execute o script `sistema_bancario_python.py` para iniciar o sistema.
3. Siga as instruções no terminal para cadastrar usuários, contas e realizar transações.

## Exemplo de Cadastro

O sistema solicita as seguintes informações para o cadastro do usuário:
- Nome
- Data de Nascimento
- CPF
- Endereço (logradouro, número, bairro, cidade/estado)