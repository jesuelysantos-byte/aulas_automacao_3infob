'''
Crie um script que usa a função quadrado
criada no arquivo exercicio_f1.py. Esse 
script deve pedir para o usuário digitar um
número, depois deve calcular o quadrado usando 
a função e depois imprimir o resultado.
'''
import exercicio_f1 as jesuely

jesuely.imprimir("Digite um número")
n1 = jesuely.ler()
jesuely.pulaLinha()
jesuely.pulaLinha()
resposta = jesuely.quadrado(n1)
jesuely.imprimir(f"O resultado é {resposta}")