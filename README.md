# Sistema Bancário

Este é um simples sistema bancário, desenvolvido em Python, onde o usuário pode realizar saques e depósitos em uma conta bancária simulada. O sistema conta com um limite diário de saques, de transações e extrato com data das operações realizadas.

![Texto alternativo da imagem](https://raw.githubusercontent.com/PedroRBrito/sistema_bancario/main/assets/menu.png) ![Texto alternativo da imagem](https://raw.githubusercontent.com/PedroRBrito/sistema_bancario/main/assets/menu_atualizado.png)

## Funcionalidades

- **Saque**: O usuário pode realizar saques de até R$500 por vez, com um limite de 3 saques diários. Caso o limite de saques ou transações seja atingido, o usuário é informado a tentar o saque no dia seguinte.
  
  ![Texto alternativo da imagem](https://raw.githubusercontent.com/PedroRBrito/sistema_bancario/main/assets/resposta_saque.png)

- **Depósito**: O usuário pode depositar valores na conta, e o saldo será atualizado. Caso o limite de transações seja atingido, o usuário também será informado.

  ![Texto alternativo da imagem](https://raw.githubusercontent.com/PedroRBrito/sistema_bancario/main/assets/resposta_deposito.png)

  
- **Extrato**: O usuário pode visualizar o histórico de saques e depósitos com sua respectiva data e hora.

  ![Texto alternativo da imagem](https://raw.githubusercontent.com/PedroRBrito/sistema_bancario/main/assets/resposta_extrato.png)

- **Verificações**: O usuário será informado do limite de valor do saque, limite de quantidade de saques e limite de transações diárias.

  ![Texto alternativo da imagem](https://raw.githubusercontent.com/PedroRBrito/sistema_bancario/main/assets/verificacao_limite_valor_saque.png) ![Texto alternativo da imagem](https://raw.githubusercontent.com/PedroRBrito/sistema_bancario/main/assets//verificacao_limite_diario_saque.png) ![Texto alternativo da imagem](https://raw.githubusercontent.com/PedroRBrito/sistema_bancario/main/assets//verificacao_limite_transacao.png)
  
- **Finalizar**: O usuário pode sair do sistema a qualquer momento.

## Instruções de uso

O sistema começa com um saldo inicial de R$1000, permitindo até 3 saques e 10 transações por dia.
O menu oferece as seguintes opções:

- **S**: Realizar um saque
- **D**: Realizar um depósito
- **E**: Consultar o extrato
- **F**: Finalizar a sessão

Ao escolher a opção de saque ou depósito, o sistema valida o valor inserido:

- Se for um valor não numérico ou negativo, o sistema pedirá um valor válido.
- Se o valor ultrapassar o limite de R$500 para saques ou for maior que o saldo disponível, o sistema informará o erro.

O extrato de transações é atualizado a cada saque ou depósito e exibido na opção **E**. Ao final de cada dia, os limites de saques e transações são resetados.

## Requisitos

- Python 3.x

## Como Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/PedroRBrito/sistema_bancario.git
