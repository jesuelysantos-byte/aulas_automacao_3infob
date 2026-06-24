'''Importar a biblioteca do pandas'''


import pandas as pd


'''Carregar uma planilha do Excel'''
'''Lê o arquivo que está no caminho e armazena na variável df'''


df = pd.read_excel("revisao/planilha.xlsx")
print(df.head())


'''Compreender funcionamento do loc'''


print(df.loc[0]) #imprime a primeira linha
print(df.loc[0, 'Nome']) #imprime a coluna Nome da primeira linha
print(df.loc[4 : 6]) #seleciona o intervalo de linhas entre 4 e 6
print(df.loc[4 : 6, "Nome"]) #seleciona a coluna Nome das linhas entre 4 e 6
print(df.loc[4 : 6, ["Nome", "Idade"]]) #seleciona as colunas Nome e Idade das linhas entre 4 e 6
print(df.loc[ : , "Nome"]) #localizar uma única coluna - todas as linhas

df2 = df.loc[3 : 6, ['Nome', 'Sexo']]
print(df2)

print(df2.loc[[True, False, False, True], ['Nome', 'Sexo']])


'''Inserir novos dados na planilha'''


df.loc[len(df)] = ["Jesuely", "Feminino", 17, "Técnico em Informática", "Automação T", 10]
print(df)


'''Atualizar dados na planilha'''


df.loc[30, ['Curso', 'Disciplina']] = ['Astronomia', 'Física']
print(df)


'''Filtrar dados'''


condicao1 = df['Idade'] == 20
condicao2 = df['Sexo'] == 'Feminino'
print(df.loc[condicao1 & condicao2, 'Nome'])


'''Classificar dados'''


tabela_ordenada = df.sort_values('Nome', ascending=False)
print(tabela_ordenada)


'''Contar dados'''


tabela_contagem = df.value_counts("Sexo")
print(tabela_contagem)


'''Agrupar dados'''


tabela_agrupada = df.groupby('Disciplina')['Nota'].sum()
print(tabela_agrupada)


'''Exportar dados'''


df.to_excel("revisao\\nova_planilha.xlsx")