#Solicitar datos
frase=input("Ingrese una frase:")

letra_remplazar=input("Ingrese una letra:")

letra_remplazarse=input("ingrese una letra que puede remplazar")

contador=frase.count(letra_remplazar)

frase_nueva=frase.replace(letra_remplazar,letra_remplazarse)

#Mostrar los valores finales

print(contador,"aparciones")

print(frase_nueva)