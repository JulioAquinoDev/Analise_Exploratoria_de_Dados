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

"""
    Listas utilizadas para obter os nomes
    de acordo com a posição e a escolha do menu de opções.
    Está sendo utilizado para imprimir os valores.
"""
PARAMETROS = ["Batimento", "Pressão", "Temperatura"]
EXPLORADOS = ["Média", "Mediana", "Desvio Padrão", "Variancia", "Valor Minimo", "Valor Máximo", "Amplitude"]

"""
  Retorna media de dois valores.
"""
def media(v1,v2):
    return (v1+v2)/2

"""
    Retorna uma matriz com
    cada item da lista obtida.
"""
def distribuirNaMatriz(a):
    x = []
    for i in a:
        y = []
        y.append(i)
        x.append(y)
    return x


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
    
    1 - Se batimento é menor que zero OU maior que 100.
    2 - Se Pressão é menor que zero OU maior que 20.
    3 - Se Temperatura é menor que zero OU maior que 40.
    
    Para cada condição com ruido, será subistituido peloa
    média do valor anterio e do próximo.
"""
for i in range(len(dados)):
    if (batimento[i] <= 0) or (batimento[i] > 100):
        batimento[i]=media(batimento[i-1],batimento[i+1])
    if (pressao[i] <= 0) or (pressao[i] > 20):
        pressao[i]=media(pressao[i-1],pressao[i+1])
    if (temperatura[i] <= 0) or (temperatura[i] > 40):
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
        5 - amplitude
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
dados_min_b = []
dados_max_b = []
dados_amp_b = []


dados_m_p = []
dados_md_p = []
dados_dp_p = []
dados_v_p = []
dados_min_p = []
dados_max_p = []
dados_amp_p = []

dados_m_t = []
dados_md_t = []
dados_dp_t = []
dados_v_t = []
dados_min_t = []
dados_max_t = []
dados_amp_t = []

for a in range(100):
    b = matriz_master[0][a]
    p = matriz_master[1][a]
    t = matriz_master[2][a]
    
    dados_m_b.append(np.average(b))
    dados_md_b.append(np.median(b))
    dados_dp_b.append(np.std(b))
    dados_v_b.append(np.var(b))
    dados_min_b.append(min(b))
    dados_max_b.append(max(b))
    dados_amp_b.append((max(b) - min(b)))
    
    
    dados_m_p.append(np.average(p))
    dados_md_p.append(np.median(p))
    dados_dp_p.append(np.std(p))
    dados_v_p.append(np.var(p))
    dados_min_p.append(min(p))
    dados_max_p.append(max(p))
    dados_amp_p.append((max(p) - min(p)))
    
    dados_m_t.append(np.average(t))
    dados_md_t.append(np.median(t))
    dados_dp_t.append(np.std(t))
    dados_v_t.append(np.var(t))
    dados_min_t.append(min(t))
    dados_max_t.append(max(t))
    dados_amp_t.append((max(t) - min(t)))
    
    u += 1

dados_b.append(dados_m_b)
dados_b.append(dados_md_b)
dados_b.append(dados_dp_b)
dados_b.append(dados_v_b)
dados_b.append(dados_min_b)
dados_b.append(dados_max_b)
dados_b.append(dados_amp_b)

dados_p.append(dados_m_p)
dados_p.append(dados_md_p)
dados_p.append(dados_dp_p)
dados_p.append(dados_v_p)
dados_p.append(dados_min_p)
dados_p.append(dados_max_p)
dados_p.append(dados_amp_p)

dados_t.append(dados_m_t)
dados_t.append(dados_md_t)
dados_t.append(dados_dp_t)
dados_t.append(dados_v_t)
dados_t.append(dados_min_t)
dados_t.append(dados_max_t)
dados_t.append(dados_amp_t)

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
    4 - Valor Minimo.
    5 - Valor maximo.
    6 - Amplitute.

C - É o valor referente ao dia.
    0 - primeiro dia.
    ...
    99 - último dia.
"""
print("------------------------------------------------")
print("5 - Análise de conteúdo.")
print("\tCorrelação entre os três parâmetros.")
auxDF=[]
auxDF+=[(float(float(matriz_master[0][0][j])),float(matriz_master[1][0][j]),float(matriz_master[2][0][j])) for j in range(0,24)]
DataFrame=[]
# MONTAGEM
DataFrame = pd.DataFrame(auxDF,columns=["BATIMENTO", "PRESSAO","TEMPERATURA"])
print(DataFrame.corr())


## criando a lista, com os dias.
dia = 100
dias = []
for i in range(dia): dias.append(i)


while True:
    print("------------------------------------------------")
    opcao_p = int(input("\n1 - Batimento.\n2 - Pressão\n3 - Temperatura\n\nQual sua opção? "))
    opcao_e = int(input("\n1 - Média.\n2 - Mediana\n3 - Desvio Padrão.\n4 - Variancia.\n5 - Valor Minimo\n6 - Valor Maximo\n7 - Amplitude.\n\nQual sua opção? "))
    print("------------------------------------------------")
    print(f"\t{EXPLORADOS[opcao_e-1]} de {PARAMETROS[opcao_p-1]} por {dia} dias.")
    plt.plot(dias, dados_extraidos[opcao_p-1][opcao_e-1])
    plt.title(f"{PARAMETROS[opcao_p-1]}")
    plt.xlabel("DIAS.")
    plt.ylabel(f"FAIXA - {EXPLORADOS[opcao_e-1]}.")
    
    """
        Essa etapa faz a
        avaliação do perfil da curva.
        Foi criado um metodo distribuirNaMatriz(X[..])
        Onde é enviado uma lista com os valores
        e retorna matriz com os valores em cada lista.
    """
    regressao=linear_model.LinearRegression()
    horas_d = np.array(distribuirNaMatriz(dias))
    valores =np.array(distribuirNaMatriz(dados_extraidos[opcao_p-1][opcao_e-1]))
    regressao.fit(horas_d,valores)
    plt.plot(horas_d, horas_d*regressao.coef_[0][0] + regressao.intercept_, color='red')
    
    plt.grid()
    plt.show()
    print("------------------------------------------------")
    print(f"\tHistograma do {PARAMETROS[opcao_p-1]}")
    # HISTOGRAMA
    hist=np.histogram(dados_extraidos[opcao_p-1][opcao_e-1])
    # PLOTAR DADOS
    plt.hist(dados_extraidos[opcao_p-1][opcao_e-1],bins='auto')
    plt.title(f"HISTOGRAMA - {PARAMETROS[opcao_p-1]} - {EXPLORADOS[opcao_e-1]}")
    plt.xlabel("FAIXA")
    plt.ylabel("OCORRENCIAS")
    plt.show()

    opcao_p = input("Deseja continuar?\nS - SIM, N - NÃO\n")
    
    if((opcao_p == "N") or (opcao_p == "n")):
        break
    
print("------------------------------------------------")