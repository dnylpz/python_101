#coding=UTF8
### Tipos de datos basicos

numero_entero = 12 #numero entero sin signo decimal
print(numero_entero)
# ademas del sistema decimal existen sistemas numericos diferentes dependiendo de la base numerica que se utilice 
# o el numero de digitos para pasar al siguiente numero ej Decimal (0-9) binario (0-1) Octal (0-8) Hexadecimal (0-f) 
numero_entero_en_binario =  0b1100 # 12 en binario 
print(numero_entero_en_binario)
numero_entero_en_octal = 0o14
print(numero_entero_en_octal)
numero_entero_en_hexadecimal = 0xc
print(numero_entero_en_hexadecimal)

print(numero_entero_en_hexadecimal == numero_entero)

# numeros con punto decimal (flotante)
numero_con_punto = 3.141592653589793
numero_con_exponente = 314e-2
numero_con_exponente_2 = 314e1
print(numero_con_exponente)

# numeros complejos (Exclusivos de python)
numero_imaginario_o_complejo = 2+3j # la j indica un numero que conocemos, se usa para representar funciones

# Caracteres (letras)
letra = 'a'
print(letra)
print(ord(letra)) #letras tambien son numeros

# caracteres especiales
letra = u"\U0001F604"
print(letra.encode('utf8'))
print(repr(letra))

# Cadenas (muchos caracteres seguidos)
cadena = "hola!"
# las cadenas no solo son palabras solas
palabras = "Hola Mundo!"

#las cadenas pueden incluir caracteres especiales como comillas o diagonales
cadena_con_especiales = "Hey You \n\"by Pink Floyd\""
print(cadena_con_especiales)

cadenas_crudas = r'Hey You \n\"by Pink Floyd\"' #cadenas que no 'escapan' los char especiales

print(cadenas_crudas)


# Cadenas con muchas lineas
parrafo = """
Lorem ipsum dolor sit amet, 
consectetur adipiscing elit. In nec felis in diam varius luctus. 
Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam auctor vitae velit sed rhoncus. 
Sed diam sapien, auctor a lacus in, ornare venenatis metus. Nam vestibulum nisi id libero rhoncus luctus. 
Sed a placerat mi. Curabitur quis nisi purus. Nullam vulputate ligula dui, quis pretium eros suscipit id. 
Cras est velit, vehicula sit amet nibh at, blandit pulvinar ex. Suspendisse potenti.
"""
print(parrafo)



# Booleanos 
verdad = True
mentira = False 

print(verdad == mentira)