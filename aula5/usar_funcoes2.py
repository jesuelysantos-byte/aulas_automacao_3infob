from aula4.funcao import imprimir
from aula4.funcao import ler, pulaLinha, somar

imprimir("Digite o número 1")
n1 = ler()
pulaLinha()
pulaLinha()
imprimir("Digite o número 2")
n2 = ler()
resposta = somar(n1, n2)
imprimir(f"O resultado é {resposta}")