#informar o nome do personagem
def main():
    print("Vou dizer a casa desse personagem")
    pers = input("Informe o nome de algum personagem de Harry Potter: ")
    pers = (pers.title())
    casa(pers)


#Verificar e mostrar qual é a casa desse personagem 
def casa(pers):
    if pers == "Harry Potter":
        print("A casa deste personagem é Grifinória")
    
    elif pers == "Hermione Granger":
        print("A casa deste personagem é Grifinória")
    
    elif pers == "Rony Weasley":
        print("A casa deste personagem é Grifinória")
    
    elif pers == "Draco Malfoy":
        print("A casa deste personagem é Sonserina")
    
    elif pers == "Luna Lovegood":
        print("A casa deste personagem é Corvinal")

    elif pers == "Cedric Diggory":
        print("A casa deste personagem é Lufa-Lufa")
    
    else:
        print("Este personagem não foi encontrado")

main()