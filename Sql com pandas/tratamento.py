import pandas as pd
import numpy as np

def Tratamento00(df):
    df["ConcluiuCurso"] = df["ConcluiuCurso"].astype(bool)
    df["AnoMatricula"] = pd.to_datetime(df["AnoMatricula"])
    df["nota1"] = df["nota1"].astype(float)
    df["nota2"] = df["nota2"].astype(float)
    df["nota3"] = df["nota3"].astype(float)
    df["nota4"] = df["nota4"].astype(float)
    return df
