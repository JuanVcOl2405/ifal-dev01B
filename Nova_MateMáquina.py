#Só dizendo oq são as coisas: "if, elif e else" são estruturas de controle, Operadores matemáticos(+, -, *, /)
# Funções: podem ser DEFindas usando o "def" (vou deixar um arquivo explicando melhor) 
print("Olá seja bem vindo(a)!")
UsarCalq = input("Gostaria de usar nossa a calculadora? (1 para sim, 2 para não, 3 para sair):")

if UsarCalq == '1':
    print("Entendido")
#O código das operações devem ficar por aqui, já que o usuario escolheu usar a matemáquina

elif UsarCalq == '2':
    print("Que pena...")

else:
    print("Saindo...")

#Esses são os códigos para colocar perto do "If"
print("soma")
def soma(a, b):
    return a + b
x = int(input("informe o valor de X:"))
y = int(input("informe o valor de y:"))

resultado_s = int(soma(x, y))
print(resultado_s)

#Subtração 
print("subtração")
def sub(a, b):
    return a - b
x = int(input("informe o valor de x:"))
y = int(input("informe o valor de x:"))

resultado_sub = int(sub(x, y))
print(resultado_sub)

#Multiplicação
print("Multiplicação")
def sub(a, b):
    return a * b

x = int(input("informe o valor de x:"))
y = int(input("informe o valor de x:"))

resultado_m = int(sub(x, y))
print(resultado_m)

#Divisão
print("Divisão")
def sub(a, b):
    return a / b 

x = int(input("informe o valor de x:"))
y = int(input("informe o valor de x:"))

resultado_d = int(sub(x, y))
print(resultado_d)


