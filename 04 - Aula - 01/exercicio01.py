# Crie um programa que o usuário digite o nome e retorna o número de caracteres.

#forma anterior
#print(len(input("Digite seu nome: ")))

nome = input("Digite seu nome: ")
tamanho_nome = len(nome)
print("O "+ str(nome) + " tem o tamanho de " + str(tamanho_nome) + " caracteres!")
