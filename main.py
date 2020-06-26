# Digamos que quieres hacer una lista de productos con precios y descripcion.
# lo podrias hacer asi
bicicleta_precio = 100.0
bicicleta_descripcion = "una bicicleta bonita"

# ahora quieres un producto diferente
pelota_precio = 10.0
pelota_descripcion = "una pelota redonda"

# evidentemente si necesitas mantener 1000 productos esto no es muy buena idea que tal que pudieramos guardar
# algunas cosas relacionadas en una sola variable?, para eso existen las colecciones o estructuras de datos, la mas basica es la lista

lista_de_precios = [100.0, 10.0]
lista_de_descripciones = ['una bicicleta bonita', 'una pelota redonda']

#si queremos acceder los datos de la bicicleta  solo tenemos que accederlos en el mismo INDICE
print("bicicleta cuesta ${} y es: {}".format(lista_de_precios[0],lista_de_descripciones[0])) #explicaremos format mas adelante
print("pelota cuesta ${} y es: {}".format(lista_de_precios[1],lista_de_descripciones[1]))

# en otros lenguajes de programacion los listas no pueden tener diferentes tipos de datos pero en python es posible

bicicleta = [100.00, 'una bicicleta bonita']
print('bicicleta cuesta ${} y es: {}'.format(bicicleta[0],bicicleta[1])) 


# side note, las cadenas tambien son como listas!, puedes acceder a sus miembros con sus indices
print('hola mundo'[0:4])


#tambien puede haber listas de listas!
pelota = [10.00, 'una pelota redonda']
productos = [bicicleta,pelota]
print(productos[1])

# puedes unir dos listas 
juguetes = [[50.00,'un muneco'],[60.00,'un carrito']]
productos = productos + juguetes
print(productos)

# en python existe otro tipo de lista, inmutable (es decir no se pueden cambiar) la tupla, la verda
# hasta ahora no recuerdo el uso de las tuplas, pero estaba chido

categorias = ('juguetes','articulos deportivos')
print(categorias)
# categorias[0] = 'comida'  # esto manda un error, intenta ver el error quitando el # al inicio de la linea

# tambien existen los sets, que son como listas pero no pueden repetir sus elementos
un_set = {'hola','mundo','hola'}
print(un_set)
#no tienen orden por lo que no puedes acceder por un indice
#print(un_set[0]) # esto manda un error
# les puedes agregar mas elementos con la funcion add
un_set.add('grande')
print(un_set)

# pero regresemos a los productos, aun con los arreglos de productos, es impractico recordar TODOS los indices, para eso existen los diccionarios

productos = {
  'bici': {
    'precio': 100.00,
    'descripcion': 'Una bicicleta bonita'
  },
  'pelota': {
    'precio': 10.00,
    'descripcion': 'una pelota redonda'
  } 
}

print(productos)
print(productos['bici']['precio'])

# regresando a las cadenas, como los arreglos tienen varias funciones para saber atributos sobre ellos despues veremos mas sobre ellos
print(len('hola mundo!!!'))
print(len(productos))
print(len(juguetes))
