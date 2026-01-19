import sqlite3 as lite

def criar_tabelas_derivadas(caminho="banco.db"):
    con = lite.connect(caminho)
    cursor = con.cursor()

    # Media
    cursor.execute("DROP TABLE IF EXISTS media")
    cursor.execute("""
        CREATE TABLE media AS
        SELECT nome,
               (nota1 + nota2 + nota3 + nota4) / 4.0 AS media
        FROM alunos
        GROUP BY nome
    """)

    # Aprovados
    cursor.execute("DROP TABLE IF EXISTS aprovados")
    cursor.execute("""
        CREATE TABLE aprovados AS
        SELECT nome
        FROM media
        WHERE media >= 7
    """)

    # Concluiu Curso
    cursor.execute("DROP TABLE IF EXISTS ConcluiuCurso")
    cursor.execute("""
        CREATE TABLE ConcluiuCurso AS
        SELECT nome
        FROM alunos
        WHERE ConcluiuCurso = 1
    """)

    con.commit()
    con.close()
