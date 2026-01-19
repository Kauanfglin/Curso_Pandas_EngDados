from criabanco import CriaBanco
from analise import criar_tabelas_derivadas
from leitura import carregar_tabela_alunos
from tratamento import Tratamento00

def main():
    CriaBanco()

    criar_tabelas_derivadas()

    df = carregar_tabela_alunos()
    df_tratado = Tratamento00(df)


    print(df_tratado)

if __name__ == "__main__":
    main()
