# -*- coding: utf-8 -*-
"""
@author: Julio
"""
 
import pandas as pd
import csv
import numpy as np
import scipy.stats as stats
import statistics as st
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.metrics import r2_score


# metodos que retorna
# media de dosi valores.
def media(v1,v2):
    return (v1+v2)/2


## leitura dos dados.
print("------------------------------------------------")
print("0 - Leitura dos dados.")
dados=[]
path = "sinaisvitais003 100dias DV2 RAxxx5.txt"
with open(path,'r',newline='') as ARQUIVO:
    d = csv.reader(ARQUIVO)
    dd=list(d)
    for i in range(0,len(dd)):
        p=dd[i][0]  
        palavras=p.split("\t")
        dados.append({"HORA":palavras[0],"BATIMENTO":palavras[1],"PRESSAO":palavras[2],"TEMPERATURA":palavras[3]}) 

print("------------------------------------------------")
print("1 - Coleta dos dados.") 
   
## Coleta dos dados. 
hora=[]
batimento=[]
pressao=[]
temperatura=[]
for i in range(0,len(dados)):
    hora.append(dados[i]["HORA"])
    batimento.append(float(dados[i]["BATIMENTO"]))
    pressao.append(float(dados[i]["PRESSAO"]))
    temperatura.append(float(dados[i]["TEMPERATURA"]))

print("------------------------------------------------")
print("2 - Limpeza dos dados.")
"""
    Exercicio 1.
    Limpeza dos dados
"""
for i in range(len(dados)):
    if (batimento[i]<0) or (batimento[i]>200):
        batimento[i]=media(batimento[i-1],batimento[i+1])
    if (pressao[i]<0) or (pressao[i]>25):
        pressao[i]=media(pressao[i-1],pressao[i+1])
    if (temperatura[i]<0) or (temperatura[i]>50):
        temperatura[i]=media(temperatura[i-1],temperatura[i+1])
print("------------------------------------------------")
print("3 - Tratamento dos dados.")
"""
    Separando os dias por dias
    contendo os registros das 24 horas.
"""
matriz_m = []
matriz_f = []

matriz_m2 = []
matriz_f2 = []

matriz_m3 = []
matriz_f3 = []

aux = 24
h = 0
# for i in range(len(dados)):
for i in range(len(dados)):
    
    matriz_f.append(batimento[i])
    matriz_f2.append(pressao[i])
    matriz_f3.append(temperatura[i])
    
    h += 1
    
    if(h == aux):
        
        matriz_m.append(matriz_f)
        matriz_m2.append(matriz_f2)
        matriz_m3.append(matriz_f3)
        
        matriz_f = []
        matriz_f2 = []
        matriz_f3 = []
        
        h = 0

matriz_master = []
matriz_master.append(matriz_m)
matriz_master.append(matriz_m2)
matriz_master.append(matriz_m3)
"""
 matriz_master[A][B][C]
 A - os parâmetros coletados.
 B - são os dias que fotam coletados, de 1 até 100.
 C - são as horas do dia. de 1 até 24.
"""

print("------------------------------------------------")
print("4 - Mineração dos dados.")
"""
    Extraindo os seguintes valores.
        1 - Média de cada dia.
        2 - Médiana de cada dia.
        3 - Desvio Padrão.
        4 - Variancia.
"""

u = 1
dados_extraidos = []
dados_b = []
dados_p = []
dados_t = []

dados_m_b = []
dados_md_b = []
dados_dp_b = []
dados_v_b = []

dados_m_p = []
dados_md_p = []
dados_dp_p = []
dados_v_p = []

dados_m_t = []
dados_md_t = []
dados_dp_t = []
dados_v_t = []

for a in range(100):
    b = matriz_master[0][a]
    p = matriz_master[1][a]
    t = matriz_master[2][a]
    
    dados_m_b.append(np.average(b))
    dados_md_b.append(np.median(b))
    dados_dp_b.append(np.std(b))
    dados_v_b.append(np.var(b))
    
    dados_m_p.append(np.average(p))
    dados_md_p.append(np.median(p))
    dados_dp_p.append(np.std(p))
    dados_v_p.append(np.var(p))
    
    dados_m_t.append(np.average(t))
    dados_md_t.append(np.median(t))
    dados_dp_t.append(np.std(t))
    dados_v_t.append(np.var(t))
    
    u += 1

dados_b.append(dados_m_b)
dados_b.append(dados_md_b)
dados_b.append(dados_dp_b)
dados_b.append(dados_v_b)

dados_p.append(dados_m_p)
dados_p.append(dados_md_p)
dados_p.append(dados_dp_p)
dados_p.append(dados_v_p)

dados_t.append(dados_m_t)
dados_t.append(dados_md_t)
dados_t.append(dados_dp_t)
dados_t.append(dados_v_t)

dados_extraidos.append(dados_b)
dados_extraidos.append(dados_p)
dados_extraidos.append(dados_t)

"""
Os valores extraidos estão
com a seguinte estrutura:

dados_extraidos[A][B][C]

A - São os Atributos.
    0 - Batimento.
    1 - Pressao.
    2 - Temperatura.

B - São os dados extraiso.
    0 - Media
    1 - Mediana.
    2 - Desvio Padrão.
    3 - Variancia

C - É o valor referente ao dia.
    0 - primeiro dia.
    ...
    99 - último dia.
"""
print("------------------------------------------------")
print("5 - Análise de conteúdo.")
dia = 100
dias = []
for i in range(dia): dias.append(i)

print(f"\tMédia de Batimento Cardiaco por {dia} dias.")
plt.scatter(dias, dados_extraidos[0][0])
plt.title(f"SCARTTER - Batimentos da amostra")
plt.xlabel("FAIXA DE DIAS")
plt.ylabel(f"FAIXA DE MEDIA de BATIMENTO")
plt.grid()
plt.show()
print("------------------------------------------------")
print(f"\tMédia de Pressão Arterial por {dia} dias.")
plt.scatter(dias, dados_extraidos[1][0])
plt.title(f"SCARTTER - Pressão Arterial da amostra")
plt.xlabel("FAIXA DE DIAS")
plt.ylabel(f"FAIXA DE MEDIA de Pressão")
plt.grid()
plt.show()
print("------------------------------------------------")
print(f"\tMédia de Temperatura Corporal por {dia} dias.")
plt.scatter(dias, dados_extraidos[2][0])
plt.title(f"SCARTTER - Temperatura Corporal da amostra")
plt.xlabel("FAIXA DE DIAS")
plt.ylabel(f"FAIXA DE MÉDIA")
plt.grid()
plt.show()
print("------------------------------------------------")
print(f"\tMediana de Batimento Cardiaco por {dia} dias.")
plt.scatter(dias, dados_extraidos[0][1])
plt.title(f"SCARTTER - Batimentos da amostra")
plt.xlabel("FAIXA DE DIA")
plt.ylabel(f"FAIXA DE MEDIANA de BATIMENTO")
plt.grid()
plt.show()
print("------------------------------------------------")
print(f"\tMediana de Pressão Arterial por {dia} dias.")
plt.scatter(dias, dados_extraidos[1][1])
plt.title(f"SCARTTER - Pressão arterial da amostra")
plt.xlabel("FAIXA DE DIA")
plt.ylabel(f"FAIXA DE MEDIANA de Pressão")
plt.grid()
plt.show()
print("------------------------------------------------")
print(f"\tMediana de Temperatura Corporal por {dia} dias.")
plt.scatter(dias, dados_extraidos[2][1])
plt.title(f"SCARTTER - Temperatura da amostra")
plt.xlabel("FAIXA DE DIA")
plt.ylabel(f"FAIXA DE MEDIANA de Temperatura")
plt.grid()
plt.show()
print("------------------------------------------------")
print(f"\tDesvio Padrão de Batimento Cardiaco por {dia} dias.")
plt.scatter(dias, dados_extraidos[0][2])
plt.title(f"SCARTTER - Batimentos da amostra")
plt.xlabel("FAIXA DE DIA")
plt.ylabel(f"FAIXA DE Desvio Padrão de BATIMENTO")
plt.grid()
plt.show()
print("------------------------------------------------")
print(f"\tDesvio Padrão de Pressão Arterial por {dia} dias.")
plt.scatter(dias, dados_extraidos[1][2])
plt.title(f"SCARTTER - Pressão arterial da amostra")
plt.xlabel("FAIXA DE DIA")
plt.ylabel(f"FAIXA DE Desvio Padrão de Pressão")
plt.grid()
plt.show()
print("------------------------------------------------")
print(f"\tDesvio Padrão de Temperatura Corporal por {dia} dias.")
plt.scatter(dias, dados_extraidos[2][2])
plt.title(f"SCARTTER - Temperatura da amostra")
plt.xlabel("FAIXA DE DIA")
plt.ylabel(f"FAIXA DE Desvio Padrão")
plt.grid()
plt.show()
print("------------------------------------------------")
print(f"\tVariancia de Batimento Cardiaco por {dia} dias.")
plt.scatter(dias, dados_extraidos[0][3])
plt.title(f"SCARTTER - Batimentos da amostra")
plt.xlabel("FAIXA DE DIA")
plt.ylabel(f"FAIXA DE Variancia")
plt.grid()
plt.show()
print("------------------------------------------------")
print(f"\tVariancia de Pressão Arterial por {dia} dias.")
plt.scatter(dias, dados_extraidos[1][3])
plt.title(f"SCARTTER - Pressão arterial da amostra")
plt.xlabel("FAIXA DE DIA")
plt.ylabel(f"FAIXA DE Variancia")
plt.grid()
plt.show()
print("------------------------------------------------")
print(f"\tVariancia de Temperatura Corporal por {dia} dias.")
plt.scatter(dias, dados_extraidos[2][3])
plt.title(f"SCARTTER - Temperatura da amostra")
plt.xlabel("FAIXA DE DIA")
plt.ylabel(f"FAIXA DE Variancia")
plt.grid()
plt.show()
print("------------------------------------------------")
print("\tCorrelação entre os três parâmetros.")
auxDF=[]
auxDF+=[(float(float(matriz_master[0][0][j])),float(matriz_master[1][0][j]),float(matriz_master[2][0][j])) for j in range(0,24)]
DataFrame=[]
# MONTAGEM
DataFrame = pd.DataFrame(auxDF,columns=["BATIMENTO", "PRESSAO","TEMPERATURA"])
print(DataFrame.corr())
print("------------------------------------------------")