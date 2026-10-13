archivo = input()
punto = archivo.find('.')
nombre_sin_ext = archivo[:punto]
extension = archivo[punto+1:]
nuevo = "MULTIMEDIA_2025_" + nombre_sin_ext + "." + extension
tamaño = str(len(nombre_sin_ext)*2)
print(nombre_sin_ext)
print(extension)
print(nuevo)
print(tamaño + " bytes")