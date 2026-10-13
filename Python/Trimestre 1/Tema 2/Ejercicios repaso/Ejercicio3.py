#Crea una función celsius_a_fahrenheit(c) que reciba una temperatura en grados Celsius y la convierta a Fahrenheit usando la fórmula: °F = (°C × 9/5) + 32

def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

temperatura_celsius = 20
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C son {temperatura_fahrenheit}°F")
