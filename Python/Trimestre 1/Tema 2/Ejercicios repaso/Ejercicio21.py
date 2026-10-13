def login():
    usuarios = {"admin": "1234", "root": "toor", "invitado": "0000"}
    intentos = 0
    while intentos < 3:
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        if usuario in usuarios and usuarios[usuario] == contraseña:
            print("Acceso concedido")
            return
        else:
            print("Credenciales incorrectas")
            intentos += 1
    print("Demasiados intentos. Acceso bloqueado.")

login()
