#condição if

#entrada
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))


#processamento
if(idade < 18):
    autorizacao = input("Os pais autorizaram a viagem? [SIM/NÃO] ")

print(f"Realizando o embarque de {nome}")
