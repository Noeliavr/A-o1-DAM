def minutos_a_horas(minutos):
    horas = minutos // 60
    resto = minutos % 60
    return horas, resto

minutos = int(input("Introduce los minutos: "))
h, m = minutos_a_horas(minutos)
print(f"{minutos} minutos equivalen a {h} horas y {m} minutos.")