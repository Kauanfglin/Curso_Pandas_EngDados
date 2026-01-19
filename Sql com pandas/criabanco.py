
import sqlite3 as sqlite3
import pandas as pd
def CriaBanco(caminho="banco.db"):
    conn = sqlite3.connect(caminho)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS alunos")

    cursor.execute("""
        CREATE TABLE alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            nota1 REAL NOT NULL,
            nota2 REAL NOT NULL,
            nota3 REAL NOT NULL,
            nota4 REAL NOT NULL,
            semestre TEXT NOT NULL,
            AnoMatricula DATE,
            ConcluiuCurso INTEGER
        )
    """)

    cursor.execute("""
        INSERT INTO alunos
        (nome, idade, nota1, nota2, nota3, nota4, semestre, AnoMatricula, ConcluiuCurso)
        VALUES
        ("João", 20, 8.5, 9.0, 7.0, 8.0, "Primeiro Semestre", "2022-01-01", 1),
        ("Maria", 21, 7.0, 6.5, 8.0, 7.0, "Segundo Semestre", "2022-02-01", 0),
        ("Pedro", 22, 9.0, 8.0, 7.0, 8.0, "Terceiro Semestre", "2022-03-01", 1),
        ("Ana", 23, 8.0, 7.5, 6.0, 7.0, "Quarto Semestre", "2022-04-01", 0),
        ("Lucas", 24, 7.0, 6.0, 8.0, 7.0, "Quinto Semestre", "2022-05-01", 1)
    """)

    conn.commit()
    conn.close()
