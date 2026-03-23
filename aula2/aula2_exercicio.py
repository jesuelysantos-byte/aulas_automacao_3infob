'''
Crie um app que solicite duas notas do usuário,
após calcule a média das notas. Se a média for maior ou igual a 6
mostre uma mensagem dizendo que o aluno está aprovado. Se a média for
menor que 6, peça para o aluno digitar a nota do exame final. Calcule
novamente a média após o exame final ((media + exame final) / 2). Se a 
média final for maior que 6, mostre a mensagem aprovado, senão mostre que 
o aluno foi reprovado
'''

n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
media = ((n1 + n2) / 2)
if media >= 6:
    print("Você foi aprovado!")

else:
    exf = float(input("Digite a nota do exame final: "))
    media_nova = ((media + exf) / 2)
    
    if media_nova >= 6:
        print("Você foi aprovado")
        
    else:
        print("Você foi reprovado")