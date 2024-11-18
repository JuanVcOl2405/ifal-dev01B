#código principal
def main(): #aprenda a perceber qual é o código principal e qual não.
    print("Diga qualquer número que digo se é par ou não")
    number = int(input("Digite um número: "))
    par(number)

#Definição fora do código: 
def par(number):
    if number % 2 == 0:
        print("É par!")
    else:
        print("É impar!")

main()