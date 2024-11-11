def main():
    print("Olá, seja bem-vindo(a)!")
    UsarCalq = input("Gostaria de usar nossa calculadora? (1 para sim, 2 para não, 3 para sair): ")

    if UsarCalq == '1':
        print("Entendido")
        OperChoose = input("Qual operação você quer usar (soma, sub, multi, div, circ): ")

        if OperChoose == 'soma':
            x = int(input("Informe o valor de x para a soma: "))
            y = int(input("Informe o valor de y para a soma: "))
            resultado_soma = soma(x, y)
            print("Resultado da soma:", round(resultado_soma))

        elif OperChoose == 'sub':
            x = int(input("Informe o valor de x para a subtração: "))
            y = int(input("Informe o valor de y para a subtração: "))
            resultado_sub = sub(x, y)
            print("Resultado da subtração:", round(resultado_sub))

        elif OperChoose == 'multi':
            x = int(input("Informe o valor de x para a multiplicação: "))
            y = int(input("Informe o valor de y para a multiplicação: "))
            resultado_multi = multi(x, y)
            print("Resultado da multiplicação:", round(resultado_multi))

        elif OperChoose == 'circ':
            raio = int(input("Informe o valor do raio para a circunferência: "))
            resultado_circ = circ(raio)
            print("Resultado da circunferência:", round(resultado_circ, 2))

        elif OperChoose == 'div':
            x = int(input("Informe o valor de x para a divisão: "))
            y = int(input("Informe o valor de y para a divisão: "))
            if y != 0:  # Evitar divisão por zero
                resultado_div = div(x, y)
                print("Resultado da divisão:", round(resultado_div, 2))
            else:
                print("Erro: Divisão por zero não é permitida.")
        else:
            print("Operação inválida.")

    elif UsarCalq == '2':
        print("Que pena...")

    elif UsarCalq == '3':
        print("Saindo...")
    else:
        print("Entrada inválida. Tente novamente.")

# Funções definidas fora dos blocos de condição
def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    return a / b

def circ(raio):
    return 3.14 * (raio * raio)

# Executa a função principal
main()
