'''
Crie um script que solicita o usuário e a senha
do estudante. Enquanto o estudante não digitar o usuário
e a senha corretamente o programa deve continuar solicitando 
as credenciais. Quando o usuário digitá-las corretamente o 
programa deve imprimir a mensagem de bem vindo e terminar.
O usuário e a senha deve ser fixo (padrão)
usuário = admin
senha = admin123
'''

while True:
    usuario = input("Digite seu login") 
    senha = input("Digite sua senha")

    if(usuario == "admin" or senha == "admin123"):
        print ("Bem vindo ao sistema")
        break
    else:
        print("Usuário ou senha inválidos")

'''/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'''

usuario = " " 
senha = " "

while (usuario != "admin" or senha != "admin123"):
    usuario = input("Digite seu login")
    senha = input("Digite sua senha")

print("Bem vindo ao sistema")