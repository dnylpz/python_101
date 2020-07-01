while True:
  print('Bienvenido a tu tienda en linea')
  print('elige una opcion')
  print('l: Ver todos los articulos')
  print('b: buscar articulo')
  print('q: salir')
  option = input()
  if option == 'l':
    print('Bicicletas')
    print('Pelotas')
    input('presiona una tecla para continuar')
  elif option == 'b':
    busqueda = input('que quieres buscar?')
    print('no encontre nada :(')
    input('presiona una tecla para continuar')
  elif option == 'q':
    break
  else:
    print('Opcion no valida! >:(')
    input('presiona una tecla para continuar')

