#Cadastro simples de dados

#Cadastro de alunos, clientes ou produtos

#Salvar e ler de arquivo

#Buscar, editar e remover registros
#Skills: listas, dicionários, CRUD básico

#cadastros = [
 #   {"id": 1, "nome": "João", "idade": 20},
  #  {"id": 2, "nome": "Maria", "idade": 25},
   # {"id": 3, "nome": "Pedro", "idade": 30}
#]

#with open("Dados.txt", "w+", encoding="utf-8") as arquivo:
 #   for cadastro in cadastros:
  #      arquivo.write(f"{cadastro['id']};{cadastro['nome']};{cadastro['idade']}\n")

   # arquivo.seek(0)  
    #Leitura = arquivo.read()

#print("Arquivo salvo com sucesso!")
#print(Leitura)

def GerarCadastroManual(cadastros):
    id = int(input("ID: "))
    nome = input("Nome: ")
    idade = int(input("Idade: "))

    cadastros.append({
        "id": id,
        "nome": nome,
        "idade": idade
    })


def Listar(cadastros):
    if not cadastros:
        print("Nenhum cadastro encontrado!")
        return

    for c in cadastros:
        print(f"ID: {c['id']}")
        print(f"Nome: {c['nome']}")
        print(f"Idade: {c['idade']}")
        print("-" * 20)


def BuscarPorId(cadastros):
    id_busca = int(input("ID: "))
    encontrado = False

    for c in cadastros:
        if c["id"] == id_busca:
            print(c)
            encontrado = True
            break

    if not encontrado:
        print("Cadastro não encontrado")


def AttCad(cadastros):
    id_editar = int(input("Qual ID deseja alterar: "))
    encontrado = False

    for c in cadastros:
        if c["id"] == id_editar:
            c["nome"] = input("Novo nome: ")
            c["idade"] = int(input("Nova idade: "))
            encontrado = True
            print("Cadastro atualizado")
            break

    if not encontrado:
        print("Cadastro não encontrado")


def RemoverCad(cadastros):
    id_remover = int(input("Qual ID deseja remover: "))
    encontrado = False

    for c in cadastros:
        if c["id"] == id_remover:
            cadastros.remove(c)
            encontrado = True
            print("Cadastro removido")
            break

    if not encontrado:
        print("Cadastro não encontrado")


def Save(cadastros):
    with open("Dados.txt", "w", encoding="utf-8") as arquivo:
        for c in cadastros:
            arquivo.write(f"{c['id']};{c['nome']};{c['idade']}\n")


def Carregar():
    cadastros = []

    try:
        with open("Dados.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                id, nome, idade = linha.strip().split(";")
                cadastros.append({
                    "id": int(id),
                    "nome": nome,
                    "idade": int(idade)
                })
    except FileNotFoundError:
        pass

    return cadastros
cadastros = Carregar()

while True:
    print("\n1-Cadastrar | 2-Listar | 3-Buscar | 4-Editar | 5-Remover | 6-Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        GerarCadastroManual(cadastros)
    elif opcao == "2":
        Listar(cadastros)
    elif opcao == "3":
        BuscarPorId(cadastros)
    elif opcao == "4":
        AttCad(cadastros)
    elif opcao == "5":
        RemoverCad(cadastros)
    elif opcao == "6":
        Save(cadastros)
        print("Dados salvos. Saindo...")
        break
    else:
        print("Opção inválida")
 