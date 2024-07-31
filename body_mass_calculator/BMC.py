# Inicio de proyecto de masa corporal
# Bienvenida del usuario
welcome  = "Bienvenido nuevo usuario a la calculadora de masa corporal"
print(welcome.capitalize())

# Solicitud e ingreso de datos

# Validación de nombres
while True:
    name = str(input("Ingrese su nombre: "))
    if all(part_name.isalpha() for part_name in name.split()) and all(man_name.istitle() for man_name in name.split()):
        break
    else:
        name_error_mensaje ="""Se dectectó una falla en el nombre.
* Utilice solo letras y esapcios.
* Solo la primera letra de cada nombre puede ir en mayuscula"""
        print(f"{name_error_mensaje}\n")

# Validación de apellidos
while True: 
    last_name = str(input("Ingrese sus apellidos: "))
    if all(part_last.isalpha() for part_last in last_name.split()) and all(man_last.istitle() for man_last in last_name.split()):
        break
    else:
        last_name_error_mensaje ="""Se dectectó una falla en el nombre.
* Utilice solo letras y esapcios.
* Solo la primera letra de cada nombre puede ir en mayuscula"""
        print(f"{last_name_error_mensaje}\n")

# body_weight = float(input('Ingrese su peso en kilogramos: \n\t kg --> '))



# height = float(input('Ingrese su peso en metros: \n\t mt: --> '))

# imc = (body_weight / height ** 2)

# if imc < 18.5:
#     print("Bajo peso") 
# elif 18.5 <= imc < 24.9:
#     print("Normal") 
# elif 25 <= imc < 29.9:
#     print("Sobrepeso") 
# else:
#     print("Obesidad") 
# print(f"{imc:.2f}")
# print(' ')