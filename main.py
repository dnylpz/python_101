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

print('\n')
# algunos operadores en python
# = asignacion
# + suma
# -  resta
# * multiplicacion
# / division
# % modulo (regresa el 'sobrante' de una division)
# ** exponente 
# // division suelo, redonde abajo numero entero mas cercano
# ejemplos
x = 5
y = 11
print(x+y)
print(x-y)
print(x*y)
print(y/x)
print(y%x)
print(x**y)
print(x//y)
print('\n')
# la asignacion se puede complementar con las operaciones
# ejemplos
x += 5 # igual a x = x + 5
x -= 5 # igual a x = x - 5 .. asi con los demas

# Operadores logicos,  estos sirven para hacer operaciones booleanas
x = True
y = False 
print( x and y) # multiplicacion booleana o es x verdad y y verdad?
print( x or y) # suma booleana o es x verdad o y verdad?
print(not y) # inversion o negacion booleana
print('\n')
# operadores de identidad, esos son para validar si algo es o no otro algo
print(x is None)
print(x is y)
print(x is not None)

print('\n')

# operadores nivel de bit
#### NAH SON MUY DIFICILES Y EN MI CARRERA NO LOS HE USADO NUNCA 
# PERO ES BUENO SABER QUE SE PUEDEN HACER OPERACIONES A NIVEL DE BIT DEL DATO SOBRE EL QUE SE APLICAN
# 
x =0b0
y = 0b111
print(x & y) 
x = 0b111
print(x & y)  #AND
print(x | y)  # OR
print(x^y) #XOR
print(~x) #NOT invierte todos los bits
print(x>>y) #shift bits right
print(x<<y) # shift bits left