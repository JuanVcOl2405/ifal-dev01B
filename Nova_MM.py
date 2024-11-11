#Só dizendo oq são as coisas: "if, elif e else" são estruturas de controle, Operadores matemáticos(+, -, *, /)
# Funções: podem ser DEFindas usando o "def" (vou deixar um arquivo explicando melhor) 
print("Olá seja bem vindo(a)!")
UsarCalq = input("Gostaria de usar nossa a calculadora? (1 para sim, 2 para não, 3 para sair):")

if UsarCalq == '1':
    print("Entendido")
    OperChoose = input("Qual operação vc quer usar:")
    if OperChoose == 'soma':
     def soma(a, b):
         return a + b
     x = int(input("informe o valor de x para a soma:"))
     y = int(input("informe o valor de y para a soma:"))
     resultado_soma = int(soma(x, y))
     print({round(resultado_soma)})
    
    if OperChoose == 'sub':
       def sub(a, b):
          return a - b
       x = int(input('informe o valor de x para a subtração:'))
       y = int(input("informe o valor de y para a subtração:"))
       resultado_sub = int(sub(x, y))
       print({round(resultado_sub)})
       
       if OperChoose == 'multi':
          def multi(a, b):
           return a * b
       x = int(input('informe o valor de x para a multiplicação:'))
       y = int(input("informe o valor de y para a multiplicação:"))
       resultado_multi = int(multi(x, y))
       print({round(resultado_multi)})

       if OperChoose == 'div':
        def div(a, b):
          return a / b
       x = int(input('informe o valor de x para a divisão:'))
       y = int(input("informe o valor de y para a divisão:"))
       resultado_div = int(div(x, y))
       print({round(resultado_div)})


elif UsarCalq == '2':
    print("Que pena...")

else:
    print("Saindo...")

