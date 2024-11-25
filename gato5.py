def main():
    miar(pegar_numero())

def miar(miaus):
    print("🐱 miau\n"* miaus, end="")

def pegar_numero():
    while True: #estrutura de loop que só irá sair se for maior ou igual a 0
        miaus = int(input("Quantas miadas: "))

        if miaus > 0:
           return miaus
main()