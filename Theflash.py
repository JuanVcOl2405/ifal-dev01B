#informar o nome do personagem

print("Vou dizer a casa desse personagem")
pers = input("Informe o nome de algum personagem: ")
 


#Verificar e mostrar qual é a casa desse personagem 
match pers:
    case "Barry Allen" | "Wally West" | "Iris West" | "Nora West-Allen" | "Bart West-Allen" | "Savitar" | "Eobard Thawne" | "Eddie Thawne" | "Jesse Chambers" | "Hunter Zolomon":
        print("Velocista")
    case "Caitlin Snow":
        print("Nevasca")
    case "Cisco Ramon" | "Cigana" | "Breacher":
        print("Vibro")
    case "Iris West-Allen" | "Joe West" | "Capitão Singh" | "Patty Spivot" | "Julian Albert" | "Linda Park" | "Sue Dibny":
        print("Humans")
    case "Cliford Devoe" | "Cecile Horton" | "Jefferson Jackson (Jax)" | "Professor Stein"| "Ronnie Raymond" | "Orlin Dwyer" | "Grace Dwyer":
        print("Metahumans")