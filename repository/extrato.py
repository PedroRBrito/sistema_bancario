def extrato(banco_usuario, cpf_login):
    print("-------------Extrato-----------")
    if not banco_usuario[cpf_login]["Conta"]["Extrato"]:
        print("Sem histórico disponível!")
    else:
        for e in banco_usuario[cpf_login]["Conta"]["Extrato"]:
            print(e)
