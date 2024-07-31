# Inicio de proyecto de masa corporal
# Bienvenida del usuario
welcome  = "Bienvenido nuevo usuario a la calculadora de masa corporal"
print(welcome.capitalize())

# Solicitud e ingreso de datos
# Validación de nombres
while True:
    name = str(input("Ingrese su nombre: "))
    if name == (""):
        print("No puede dejar campos vacios\n ")
    elif all(part_name.isalpha() for part_name in name.split()) and all(man_name.istitle() for man_name in name.split()):
        # el itinerante creado hara que la variable part_name contenga
        # part_name [primer nombre, segundo nombre]
        break
    else:
        name_error_mensaje ="""Se dectectó una falla en el nombre.
* Utilice solo letras y esapcios.
* Solo la primera letra de cada nombre puede ir en mayuscula"""
        print(f"{name_error_mensaje}\n")

# Validación de apellidos
while True: 
    last_name = str(input("Ingrese sus apellidos: "))
    if last_name == "":
        print("No puede dejar campos vacios.\n")
    elif all(part_last.isalpha() for part_last in last_name.split()) and all(man_last.istitle() for man_last in last_name.split()):
        break
    else:
        last_name_error_mensaje ="""Se dectectó una falla en el nombre.
* Utilice solo letras y esapcios.
* Solo la primera letra de cada nombre puede ir en mayuscula"""
        print(f"{last_name_error_mensaje}\n")

while True:
    body_weight = input('Ingrese su peso en kilogramos: \n\t kg --> ')
    # Verificación de esapcio en blanco, cantidaes negativas y exceso de puntos decimales
    if body_weight == "":
        print("No puede dejar campos vacios\n")
    elif body_weight.count(".") > 1:
        print("Solo puede usar un punto decimal.")
    elif (body_weight.count("-") > 1) or (body_weight.count("-") == 1 and body_weight.count("0")):
        print ("No se permite el uso de cantidades negativas")
    else:
        # División en dos partes desde el punto decimal para luego verificar con .isdigit si se cumplen
        body_weight_parts = body_weight.split(".")
        entire_part = body_weight_parts[0]
        decimal_part = body_weight_parts[1] if len(body_weight_parts) > 1 else ""
        # Verificación de partes núemricas
        if ((entire_part.isdigit()) and (decimal_part.isdigit()) or decimal_part == ""):
        # Convertimos la variable a float descpues de la verificación.
            body_weight = float(body_weight)
            break
        else:
            print("Se detectó un fallo.\nSolo puede ingresar números.")
print(type(body_weight))

while True:
    height = input('Ingrese su altura en metros en metros: \n\t mt: --> ')
    if height == (""):
        print ("No puede dejar campos vacios\n")
    elif height.count(".") > 1:
        print("Solo se puede usar un punto decimal")
    elif ((height.count("-") > 1) or ((height.count("-") == 1 ) and height.count("0"))):
        print("No se permiten cantidades negativas o iguales a 0")
    else:
        height_parts = height.split(".")
        heights_entire_part = height_parts [0]
        heights_decimal_part = height_parts [1] if len(height_parts) > 1 else ""
        # Verificación de las partes númericas
        if (heights_entire_part.isdigit() and heights_decimal_part.isdigit() or heights_decimal_part == ""):
            #Conversión de cantidad a float
            height = float(height)
            break
        else:
            print("Se detectó un error\nSolo puede ingresar números")
# Verificación del proceso y verificación de las variables
print(f"Los datos recolectados son: {name}, {last_name}, {body_weight}, {height}")


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