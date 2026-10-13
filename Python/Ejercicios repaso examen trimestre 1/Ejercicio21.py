def login():
    lista_usuarios = ["admin", "root", "invitado"]
    lista_contraseña = ["1234", "toor", "0000"]
    intentos = 0
    while intentos < 3:
        usuario = input("Dime el usuario: ")
        contraseña = input ("Dime la contraseña: ")
        for u in range(len(lista_usuarios)):
            if lista_usuarios[u] == usuario and lista_contraseña[u] == contraseña:
                print ("Acesso concedido")
                return
        print ("Intentelo de nuevo")
        intentos += 1
    print("Numero de intentos superados")
login()