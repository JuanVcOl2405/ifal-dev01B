while True: #estrutura de loop que só irá sair se for maior ou igual a 0
    miaus = int(input("Quantas miadas: "))

    if miaus > 0:
        break

print("🐱 miau\n"* miaus, END="")