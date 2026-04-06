import aula4.funcao as jesuely

jesuely.imprimir("Digite o número 1")
n1 = jesuely.ler()
jesuely.pulaLinha()
jesuely.pulaLinha()
jesuely.imprimir("Digite o número 2")
n2 = jesuely.ler()
resposta = jesuely.somar(n1, n2)
jesuely.imprimir(f"O resultado é {resposta}")