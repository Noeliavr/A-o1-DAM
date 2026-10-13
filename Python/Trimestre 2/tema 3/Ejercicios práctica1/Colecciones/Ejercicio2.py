def lista (numero:list, nuevo:float):
    numero =[4, 2, 5, 1, 3]
    print (numero)
    nuevo=0
    numero.insert(0,nuevo)
    print (numero)
    numero.sort()
    print (numero)
    medio = (len(numero) //2)-1
    del numero[medio]
    print(numero)
