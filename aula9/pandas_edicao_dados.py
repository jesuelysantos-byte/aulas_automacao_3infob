#Pandas: Biblioteca em Python que permite a manipulação de arquivos
#em formato tabular, ex: Planilhas e Tabelas

#Edição de Dados (Inserir, Atualizar e Excluir)

#Instalação 
#pip install pandas

#Importar biblioteca (as renomeia o pacote "abreviação")
import pandas as pd

#Ler uma planilha do Excel
#Cria a variável planilha que vai guardar a planilha do Excel
#Em pandas chamamos a planilha de DataFrame
planilha = pd.read_excel("aula9\\Dados_3INFOB.xlsx")

#Imprime os dados da planilha
print(planilha)

#Imprime a cabeça da planilha: Quantas linhas da parte de cima eu quero imprimir
print(planilha.head(6))

#Imprimir as últimas 3 linhas
#print(planilha.tail(5))

nova = planilha.head(4)
print(nova.tail(2))

#Inserir um novo registro na Planilha
planilha.loc[len(planilha)] = ['Pablo', 52, 1.8, 'M']
print(planilha)

#Atualizar um registro
planilha.loc[16] = ['Pablo', 52, 1.8, 'Masculino']
print(planilha)

#Atualizar um registro, apenas uma coluna
planilha.loc[16, 'Nome'] = 'Pablo Sandi'
print(planilha)

#Atualizar um registro, duas ou mais colunas
planilha.loc[16, ['Peso', 'Altura']] = [53, 1.81]
print(planilha)

#Remover um registro da planilha
planilha.drop(13, inplace=True)
print(planilha)