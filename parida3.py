#código principal
def main(): #aprenda a perceber qual é o código principal e qual não.
    print("Diga qualquer número que digo se é par ou não")
    number = int(input("Digite um número: "))
    print("É par") if par(number) else print("É impar")

#Definição fora do código: 
def par(number):
    return number % 2 == 0 

main()