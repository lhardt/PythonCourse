# Converter uma temperatura de °C para °F
# Fórmula: Tf = 9Tc/5 + 32

temp_celsius = float(input("Qual é a temperatura em Celsius? "))

temp_fahr = 9 * temp_celsius / 5  + 32

print('{:.1f}°C é correspondente a: {:.1f}°F'.format(temp_celsius, temp_fahr))
