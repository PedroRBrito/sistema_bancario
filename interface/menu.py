def menu_conta(banco_usuario, cpf_login):
    
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

def menu_inicial():
    return input(f"""
-----------Bem-Vindo----------
                 
Qual das opções quer seguir?

[L] Login                
[C] Listar Contas
[S] Sair
                 
------------------------------

""").strip()



def listar_contas(banco_usuario):
    print("-------------Lista de contas------------\n")
    for cpf, dados_usuario in banco_usuario.items():
        nome = dados_usuario['Nome']
        print(
f"""    Nome: {nome}             
    Agência: {dados_usuario['Conta']['Agência']}
    Conta: {dados_usuario['Conta']['Número da conta']}

----------------------------------------
""")
    return banco_usuario