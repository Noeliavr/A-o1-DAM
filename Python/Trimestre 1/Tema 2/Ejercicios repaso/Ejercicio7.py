def validar_contraseña(clave):
    tiene_mayus = any(c.isupper() for c in clave)
    tiene_num = any(c.isdigit() for c in clave)
    return len(clave) >= 8 and tiene_mayus and tiene_num

pwd = input("Introduce una contraseña: ")
if validar_contraseña(pwd):
    print("Contraseña válida ")
else:
    print("Contraseña no válida (mínimo 8 caracteres, 1 mayúscula y 1 número)")