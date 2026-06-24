import pandas as pd
alunos = pd.read_excel("aula10\\dados.xlsx", sheet_name="alunos")

print(alunos.head(5))

alunos.loc[len(alunos)] = [8, "Enzo Moreira", "Técnico em Jogos", "1GMA"]
print(alunos)

alunos.loc[alunos['Nome'] == 'Enzo Moreira', ['Curso', 'Turma']] = ["Técnico em Informática", "3TE"]
print(alunos)

alunos.drop(0, inplace=True)
print(alunos)

alunos.to_excel("nova_planilha.xlsx", index=False)

curso = alunos.loc[alunos['Curso'] == 'Técnico em Informática']
print(curso)