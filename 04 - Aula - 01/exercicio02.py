# Crie um programa que o usuário digite 2 valorese apareça a soma

# Esse gerou erro 1 + 1 = 11
#print((input("Informe o primeiro número: ") + input("Informe o segundo número: "))) 

# Esse gerou erro : Não recebe números com casa decimal
#print((int(input("Informe o primeiro número: ")) + int(input("Informe o segundo número: ") ) ) ) 

print((float(input("Informe o primeiro número: ")) + float(input("Informe o segundo número: ") ) ) ) 

#variaveis primitiva

#int
numero = 3                  
print(type(numero))

#float
numero_decimal = 4.78       

#string
nome_de_usuario = "Thiago"  

#boll
verdadeiro = True           

#contant
SENHA = "senha"

# Variavel oculta
_SENHA = "Ocultar variavel"


#CUIDADO ao setar valor a variavel
#As variaveis não são tipadas ou seja uma variavel pode receber valor distinto. Exemplo :

variavel_exemplo = numero
print(type(variavel_exemplo))
print(variavel_exemplo)

variavel_exemplo = numero_decimal
print(type(variavel_exemplo))
print(variavel_exemplo)

variavel_exemplo = nome_de_usuario
print(type(variavel_exemplo))
print(variavel_exemplo)

variavel_exemplo = verdadeiro
print(type(variavel_exemplo))
print(variavel_exemplo)

