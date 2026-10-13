email = input()
usuario = email[:email.find('@')]
dominio = email[email.find('@')+1:]
print(usuario)
print(dominio)
print(str(len(email)))
if usuario.count("0")+usuario.count("1")+usuario.count("2")+usuario.count("3")+usuario.count("4")+usuario.count("5")+usuario.count("6")+usuario.count("7")+usuario.count("8")+usuario.count("9") > 0:
    print("Sí")
else:
    print("No")