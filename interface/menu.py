def menu(banco_usuario, cpf_login):
    
    return input(f"""
----------Informações---------
Cliente: {banco_usuario[cpf_login]["Nome"]}
Saldo : {banco_usuario[cpf_login]["Conta"]["Saldo"]:0.2f}
Saques restantes: {banco_usuario[cpf_login]["Conta"]["Quantidade de saques"]}
Transações Restantes: {banco_usuario[cpf_login]["Conta"]["Quantidade de transações"]}
-------------Menu--------------                                  
[S] Saque                         |
[D] Depósito                      |
[E] Extrato                       |
[T] Trocar de conta ou sair       |
-------------------------------

""").strip()

def login():

    return input(f"""
-------------Login------------
                 
Digite seu CPF:
                 
------------------------------

""").strip()

def encerrar():
    return input(f"""
-------------Aviso------------
                 
Qual das opções quer seguir?

[T] Trocar de conta                 
[S] Sair
                 
------------------------------

""").strip()