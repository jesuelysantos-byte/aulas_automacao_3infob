#Estrutura de Repetição: Utilizando para repetir um conjunto
#Instruções - comandos, quando sabemos quantas vezes a instrução deve ser repetida

#Exemplo 1
#for variavel in range(valor inicial, valor final, passo)
#range -> intervalo de valores

#range(1, 10, 1): Intervalo gerado -> 1, 2, 3, 4, 5, 6, 7, 8, 9
for i in range(1,10,1):
    print(i, end=" ")

print("\n")

#range(1, 7, 2): Intervalo gerado -> 1, 3, 5
for i in range (1,7,2):
    print(i, end=" ")

print("\n")

#range(0, -4, -1): Intervalo gerado -> 0, -1, -2, -3
for i in range (0,-4,-1):
    print (i, end=" ")
print("\n")

#range(10): Intervalo gerado -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
for i in range (10):
    print(i, end=" ")