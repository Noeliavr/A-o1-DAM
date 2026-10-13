
def es_primo(n):
    if n%2!=0 and n>1 and n%3!=0 and n%5!=0:
        return True
    else:
        return False
    
    
numero=int(input("numero: "))
if es_primo(numero):
    print("True")
else:
    print("False")

