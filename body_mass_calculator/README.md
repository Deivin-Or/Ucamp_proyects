# Calculadora de masa corporal

Programa escrito en lenguaje python, dirigido al proceso de calculo de masa corporal de un individuo de minimo un año de edad.

Datos que puede procesar el programa:

Nombre de usuario: puedo aceptar más de un nombre (Siempre y caundo sea de la msima persona), con inicial myaúscula, por lo cual al ingresar nombre con mayúscaulas faltas y/o mezcladas repetira el proceso de registro, además que vuelve a pedir los datos en dado caso que sea haya introducido algun dato que no fuera un letra del alfabeto.

Apellido de usuario: es el mismo proceso con el nombre de usuario, solo acepta mayúscaulas al inicio de cada nombre y no permite mezclar letras con números.

Edad de usuario: Se registra como un dato de seguimiento, sin embargo se planea utilizarlo en un a versión posteriror si se diera la oportunidad de una nueva actualización, se aclara que este solo admite números y al ingresar letras este le pedirá que ingrese su edad de nuevo además que se agregó una nueva función que limita la edad que se puede ingresar cuyo limite no pude igualar o superar 200 años.

Peso del usuario: el peso está programado en kilogramos y no admite letras dentro del ingreso de este dato.

Altura del usuario: está esta definida en metros y no admite letras al ingreso de datos.

La formula utilizada dentro de está es la estandar (Peso/Altura^2).

OJO: Todos las entradas de datos no admiten espacios vacios o nulos, además en los secciones de edad, peso y altura del usuario no admiten cantidades nulas como "0" y/o "0000", esto con la finalidada de evitar error en el procesamiento e impresión de los datos finales.

Resultados del usuario: las impresiones cambiarán dependiendo de los datos y con una frase acampañada de un emoticon, para que el usuario sea consiente de cauta masa corporal posee.

Proximas actualizaciones: 
Se pretende en un futuro una versión que no solo se base un una sola formúla para calcular el IMC si no que támbien incluir una tabla de masa corporal según años (Para los niños) y recomendaciones (Para los adultos), además de procesar los datos de menors de un año.

Peso  de archivos: 9 Kb.

Notas de código:

Nombres y apellidos: Se utilizaron funciones de cadenas y procesos de valores como and y or, estos para validar que la división de de la variable al convertirla en itineran pueda procesar si se inicia con mayúscula y que no admita números dentro de ella, se hizo un casteo a str (Aunque por los strings simepre devuleve un str por defecto).

Edad: se utilizo casi el msimo proceso con nombre y apellidos, ya que el casteo se hizo al final ya que se necesita que la variables este en string para que las funciones de cade pudedan verificar que no se haya cometido un error al ingresar los datos.

Peso y Altura: (Que desde mi perspectiva la parte más dificil de programar de está calcculadora) a la falta de cadenas que verifiquen puntos como si fueran decimales opte por hacer un código que identificará primero si habria valoes negativos o puntos decimales de más (Cuya respueta la encotré en la función .count) asi que al pasar los proceso de identificación de errores (Parecidos a a los que se utilizaron en edad) se continueo con el proceso de separado usando la función de split pero con la diferencia que esta tendría un como limte el punto para separar, a si al separa las variable podria verificar n la parte entera y decimal si ambos habían ingresado números, pero en la parte decimal tendría que definar la longitud de los carecteres despues del punto fueran mayores que cero apartir del indice 1 (Por el punto decimal) y si este no cumple se le dará un espacio vacio, ya que nos referemos a un número exacto, al verificar que se haya cumplido con la condición que sean números en ambas partes se procede a unirlas en una variable y cateralas a un tipo float.

Nota: las variables están en inglés como forma de práctica de escritura de código y se ulitilizó la nomenclatura de variables SNACKE_CASE.

Resultados: con la finalidad de dar una respuesta un poco más atrayente y facíl de enteder al ususrio se agregón una lisat de constantes, que cada una lleva el código de color, ademas que en cada serulatado fue separdao con su correpondiente if, elif (Para respuestas exta) y else (Se no entraba en ninguna categoria), estos se agregaron y van cambaindo de contenido para dar un un mensaje y emoticon diferente dependiendo de la situación (Esto gracias al tipado deinamico de Python), y no se usaron prints por cada respuesta, ya que para que el código se más legible (En mi caso lo senti un pco más entendible), se realizó la repsueta en un print formateado ya que de esa forma se pueden sustituir más facilmente las variables dentro de las mismas.

Nota: los colores puden pintar toda la repsuesta desde donde se le indique la variable format_color es solo el color por default para que está funcione como tipo de limitador de hasta donde queremos colorear.

Muchas Gracias por usar mi código.
