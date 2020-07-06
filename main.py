productos = [{
    'upc': 22345632465,
    'nombre': 'bicicleta',
    'precio': 10.0,
    'descripcion': 'Roja, Rodada 26\"'
  },
  {
    'upc': 2364325234,
    'nombre': 'pelota',
    'precio': 5.0,
    'descripcion': 'Futbol'
  },
  {
    'upc': 512348235123,
    'nombre': 'monopoly',
    'precio': 8.00,
    'descripcion': 'Hashbro'
  },
]


while True:
  print('Bienvenido a tu tienda en linea')
  print('elige una opcion')
  print('l: Ver todos los articulos')
  print('b: buscar articulo')
  print('q: salir')
  option = input()
  if option == 'l':
    while True:
      print('ordenar los articulos por ')
      print('1.- nombre')
      print('2.- UPC')
      print('3.- precio')
      print('4.- regresar')
      order = input('seleccione opcion')
      if order == '1':
        for i in range(0,len(productos)):
          for j in range(0,len(productos)-i-1):
            if(productos[j]['nombre'] > productos[j+1]['nombre']):
              temp = productos[j+1]
              productos[j+1] = productos[j]
              productos[j] = temp
        print(productos)
      elif order == '2':
        pass
      elif order == '3':
        pass
      elif order == '4':
        break
      else:
        print('opcion no valida')
      input('presiona una tecla para continuar')
  elif option == 'b':
    busqueda = input('que quieres buscar?\n')
    found = False
    for producto in productos:
      if busqueda in producto['nombre']:
        print(producto['nombre'])
        found = True
        break        
    if not found: 
      print('no encontre nada :(')
    input('presiona una tecla para continuar')
  elif option == 'q':
    break
  else:
    print('Opcion no valida! >:(')
    input('presiona una tecla para continuar')

