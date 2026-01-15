# NÍVEL INICIANTE (Base em Python)

# Objetivo: lógica, listas, dicionários, arquivos

# Leitor e analisador de arquivos

#Ler arquivos .txt ou .csv

#Contar linhas, palavras, números

#Gerar um resumo final
#Skills: open(), loops, strings


with open('lorem.txt', 'r', encoding='utf-8') as Arquivo:
    texto = Arquivo.read()

palavras = texto.split()
contador = 0
contadorN = 0
for index in range(len(palavras)):
    if len(palavras[index]) > 0:
        contador += 1
    if palavras[index].isnumeric():
        contadorN += 1    
print(f"O arquivo possui {contador} palavras.") 
print(f"O arquivo possui {contadorN} números.")


with open('lorem.txt','r',encoding='utf-8') as Arquivo:
    texto = Arquivo.read()
linhas = texto.split('\n')
contador = 0
contadorN = 0
for i in range(len(linhas)):
    if len(linhas[i]) > 0:
        contador += 1
    if linhas[i].isnumeric():
        contadorN += 1
print(f"O arquivo possui {contador} linhas.")
print(f"O arquivo possui {contadorN} números.")

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

with open('lorem.txt', 'r', encoding='utf-8') as Arquivo:
    texto = Arquivo.read()
parser = PlaintextParser.from_string(texto, Tokenizer("portuguese"))
sumario = LsaSummarizer().summarize(parser.document, 3)
print(f"Resumario: {sumario}")