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

#Validación de edad
while True:
    old_years = input("Ingrese su edad en años \n \t--> ")
    if old_years == "":
        print("No se permite dejar espacios en blanco")
    elif all(old_years_zero == "0" for old_years_zero in old_years):
        print ("Ingrese una cantidad válida\n Próximas... actualizaciones podra ingresa edades menores a 1 año.\n")
    elif not old_years.isdigit():
        old_years_error_mensage = """Se detectó un error
Verifique lo siguiente:
* No se permité el uso de letras
* Evite el uso de decimales o comas."""
        print(f"{old_years_error_mensage}\n")
    else:
        old_years = int(old_years)
        if old_years >= 200:
            old_years_inmortal = """Lo siento está calculadora no tiene los permisos suficientes 
para analizar los datos de viajeros e inmortales.
* Verifique su edad y vuelva a inetntarlo."""
            print(f"{old_years_inmortal}\n")
        else:
            break

# Validación de peso
while True:
    body_weight = input('Ingrese su peso en kilogramos: \n\t kg --> ')
    # Verificación de esapcio en blanco, cantidaes negativas y exceso de puntos decimales
    if body_weight == "":
        print("No puede dejar campos vacios\n")
    elif body_weight.count(".") > 1:
        print("Solo puede usar un punto decimal.\n")
    elif (body_weight.count("-") >= 1):
        print("No se permiten cantidades negativas\n")
    elif all(zero == "0" for zero in body_weight):
        print ("No se permite el uso de cantidades iguales a cero\n")
    else:
        # División en dos partes desde el punto decimal para luego verificar con .isdigit si se cumplen
        body_weight_parts = body_weight.split(".")
        entire_part = body_weight_parts[0]
        decimal_part = body_weight_parts[1] if len(body_weight_parts) > 1 else ""
        # Verificación de partes núemricas
        if entire_part.isdigit() and (decimal_part.isdigit() or decimal_part == ""):
        # Convertimos la variable a float descpues de la verificación.
            body_weight = float(body_weight)
            break
        else:
            print("Se detectó un fallo.\nSolo puede ingresar números.\n") 
# print(type(body_weight))

# Validación de altura
while True:
    height = input('Ingrese su altura en metros en metros: \n\t mt: --> ')
    if height == (""):
        print ("No puede dejar campos vacios\n")
    elif height.count(".") > 1:
        print("Solo se puede usar un punto decimal\n")
    elif ((height.count("-") > 1) or (height.count("-") == 1 )):
        print("No se permiten cantidades negativas\n")
    elif all(zero_height == "0" for zero_height in height):
        print ("No se permite el uso de cantidades iguales a cero\n")
    else:
        height_parts = height.split(".")
        heights_entire_part = height_parts [0]
        heights_decimal_part = height_parts [1] if len(height_parts) > 1 else ""
        # Verificación de las partes númericas
        if heights_entire_part.isdigit() and (heights_decimal_part.isdigit() or heights_decimal_part == ""):
            #Conversión de cantidad a float
            height = float(height)
            break
        else:
            print("Se detectó un error\nSolo puede ingresar números\n")

# Verificación del proceso y verificación de las variables
# print(f"Los datos recolectados son: {name}, {last_name}, {body_weight}, {height}")

# Proceso matemático
imc = (body_weight / height ** 2)

# Variables de color.
BLUE = ("\033[94m")
GREEN = ("\033[92m")
GREEN_DARK = ("\033[32m")
YELLOW = ("\033[93m")
ORANGE = ("\033[33m")
RED = ("\033[91m")
RESET_COLOR = ("\033[0m")

if imc < 18.5:
    symbol = ("🔵🍔🍝")
    category = (f"{BLUE}Bajo peso{RESET_COLOR}")
    motivation = ("Necesitas alimentarte mejor")
elif imc >= 18.5 and imc < 24.9:
    symbol = ("💚💪🏆")
    category = (f"{GREEN}Normal{RESET_COLOR}")
    motivation = ("Muy bien alimentadote y ejercitandote así.")
elif imc >= 25 and imc < 29.9:
    symbol = ("🟢⚽🏃‍♂️")
    category = (f"{GREEN_DARK}Sobrepeso{RESET_COLOR}")
    motivation = ("Un taquito menos no te mueres de hambre")
elif imc >= 30 and imc < 34.9:
    symbol = ("🟡🥦🧗‍♀️")
    category = (f"{YELLOW}Obesidad I{RESET_COLOR}")
    motivation = ("Necesitas empezar a cuidar tu alimentación y elige un deporte que te guste.")
elif imc >= 35 and imc < 39.9:
    symbol = ("🟠🏋️❗")
    category = (f"{ORANGE}Obesidad II{RESET_COLOR}")
    motivation = ("Ve a examinarte para comenzzar una dieta y deporte riguroso, los necesitas.")
else:
    symbol = ("🔴⚠️🧑‍⚕️")
    category = (f"{RED}Obesidad III{RESET_COLOR}")
    motivation = ("Ve a examinarte para comenzzar una dieta y deporte riguroso, los necesitas.")

print(f"""
-------------------------------------------------------------
Sus resultados son: 
Nombres: {name}
Apelidos: {last_name}
Edad: {old_years}
Peso {body_weight} y Altura {height} ingresados
Su IMC es de:{imc:.2f} {category} 
Cometario: {motivation} {symbol}
-------------------------------------------------------------""")

print('\nGracias por usar nuestra calculadora.')