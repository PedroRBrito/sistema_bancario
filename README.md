# Sistema Bancário

Esse é um projeto de um **sistema bancário** simples, implementado em Python, com funcionalidades como cadastro de usuários, login, saque, depósito, extrato de conta e gerenciamento de transações.

## Funcionalidades

- **Login de usuário**: O sistema permite que o usuário faça login usando seu CPF.
- **Cadastro de novo usuário e conta**: Caso o CPF não exista, o sistema permite o cadastro de um novo usuário e sua conta bancária.
- **Saque**: O usuário pode realizar saques na sua conta, conforme as regras de transações.
- **Depósito**: O usuário pode realizar depósitos na sua conta.
- **Extrato**: O usuário pode verificar seu extrato bancário.
- **Lista de contas**: O sistema permite listar todas as contas cadastradas.
- **Encerramento**: O sistema pode ser encerrado a qualquer momento.

## Estrutura do projeto

- **`core/`**: Contém as funcionalidades principais como transações, conta e regras bancárias.
- **`repository/`**: Contém funcionalidades de extrato.
- **`interface/`**: Contém o menu e interações com o usuário.
- **`services/`**: Contém a lógica de regras bancárias.
- **`sistema_bancario.py`**: Arquivo principal que executa o sistema.

## Como usar

1. Clone o repositório:
    ```bash
    git clone https://github.com/seuusuario/sistema-bancario.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd sistema-bancario
    ```

3. Execute o script principal:
    ```bash
    python sistema_bancario.py
    ```

4. Siga as instruções do menu interativo para realizar operações bancárias.


## Tecnologias usadas

- **Python 3.x**: Linguagem de programação utilizada.
- **Datetime**: Para manipulação de datas e registros de transações.