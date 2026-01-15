# Limpeza de dados simples

#Receber lista com dados errados (None, strings vazias)

#Limpar e padronizar
#Skills: condicionais, funções


dados_sujos = [
    " Ana ",
    None,
    "",
    "CARLOS",
    "   ",
    "maria",
    25,
    " João ",
    None
]
def Limpar_Dados(dados_sujos):
    dados_limpos = []

    for dado in dados_sujos:

        #  Remove None
        if dado is None:
            continue

        #  Garante que é string
        if not isinstance(dado, str):
            continue

        #  Remove espaços
        dado = dado.strip()

        # Remove string vazia
        if dado == "":
            continue

        #  Adiciona dado limpo
        dados_limpos.append(dado)

    return dados_limpos


Add = Limpar_Dados(dados_sujos)

print(Add)



def limpar(dadosS):
    tratamento = []

    for dado in dadosS:
        if dado is not None and isinstance(dado, str):
            dado = dado.strip()
            if dado != "":
                tratamento.append(dado)

    return tratamento

print(limpar(dados_sujos))