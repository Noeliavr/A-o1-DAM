nombre = input()
diseno = input()
programacion = input()
audio = input()
media = (float(diseno)+float(programacion)+float(audio))/3
partes = nombre.split()
codigo = partes[0][:2].upper() + partes[1][:2].upper() + str(media).replace('.', '')[-2:]
print(nombre)
print(str(media))
print(codigo)