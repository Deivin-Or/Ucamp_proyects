# Inicio de proyecto de masa corporal

body_weight = float(input('Ingrese su peso en kilogramos: \n\t kg --> '))
height = float(input('Ingrese su peso en metros: \n\t mt: --> '))

imc = (body_weight / height ** 2)

print(f"{imc:.2f}")