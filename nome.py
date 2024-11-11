nome = input("Digite seu nome:")
#print("olá,", end=" ")
#print(nome)
 
 #Aula de methods_string
#nome = nome.title().strip()
#print(f"Olá, {nome.lower}")
#print(f"Olá, {nome.upper}")
#print(f"Olá, {nome.title}") 

#".split" "fatia" os espaços vazios
nome, sobrenome = nome.split()
#esse "nome + " " + sobrenome" se chama contatenar
nome_completo = nome + " " + sobrenome

#".title" deixa em formato de tetxo: "ok, amigo" => "Ok, amigo"
print(f"Olá, {nome_completo.title()}")