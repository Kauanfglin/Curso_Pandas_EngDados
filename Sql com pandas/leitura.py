import pandas as pd
import sqlite3 as lite

def carregar_tabela_alunos(caminho="banco.db"):
    con = lite.connect(caminho)
    df = pd.read_sql_query("SELECT * FROM alunos", con)
    con.close()
    return df
