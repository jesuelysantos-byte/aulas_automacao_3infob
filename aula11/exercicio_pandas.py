import pandas as pd

alunos = pd.read_excel('aula11\\notas_estudantes.xlsx')
df_notas = pd.read_excel('aula11\\notas_estudantes.xlsx', sheet_name='Notas')
df_atividades = pd.read_excel('aula11\\notas_estudantes.xlsx', sheet_name='Atividades')

print(df_notas)
print(df_atividades)

'''
'''
df_notas.loc[len(df_notas)] = ["Lucas Silva", "Prova Final", "8.5"]
print(df_notas)

'''
'''
df_notas.loc[1, ['Nota']] = [9.0]
print(df_notas)

'''
'''
df_notas = df_notas.drop(
    df_notas[
        (df_notas['Nome'] == 'Pedro Santos') &
        (df_notas['Atividade'] == 'Prova 1')
    ].index
)
'''
'''
notas_maiores_que_7 = df_notas[df_notas['Nota'] > 7.0]
print(notas_maiores_que_7)
'''
'''
nome_nota = df_notas[['Nome', 'Nota']]
print(nome_nota)
'''
'''
prova_final = df_notas[df_notas['Atividade'] == 'Prova Final']
print(prova_final)
'''
'''
alunos_aprovados = df_notas[df_notas['Nota'] > 7.0][['Nome', 'Atividade']]
print(alunos_aprovados)
'''
'''
