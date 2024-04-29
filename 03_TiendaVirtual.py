#Proyecto 03 - Tienda Virtual
#Programa que simule una tienda virtual simple
#Especificaciones:
#Muestra un catálogo de productos disponibles con sus nombres y precios.
#EI usuario deberá tener la opción de agregar productos al earrito.
#EI usuario deberá tener la opción de ver lo que hay en el carrito.
#EI usuario deberá tener la opción de realizar el pago y salir.
#EI usuario deberá tener la opción de salir sin comprar
print('\nTIENDA VIRTUAL\n')
menu = ['Agregar productos al carrito', 'Ver carrito','Realizar el pago y salir','Salir']
productos = [['Camiseta',20], ['Jeans',40],['Zapatos',60],['Sombreros',10],['Chalecos',10]]
carrito = []

while True:
    duplicado = False
    existe = False
    print('\nMENÚ:')
    for i in range(len(menu)):
        print(f'{i+1}. {menu[i]}')
    try:
        opcion = int(input('Seleccione una opción: '))
        if opcion == 1:
            print('\n\nAgregar productos al carrito:')
            print(''.rjust(29,"="))
            print('Productos disponibles:')
            print('PRODUCTO'.rjust(20),'PRECIO'.rjust(20))
            print('--------'.rjust(20),'------'.rjust(20))
            for producto, precio in productos:
                print('.',f'{producto}'.center(28),f'S/{precio} c/u'.rjust(11))
                
            agregar = input('|=> Ingrese el nombre del producto que deseas comprar: ').lower()
            #Saber si esta en carrito solo aumentar cantidad
            for j in range(len(carrito)):
                if agregar == carrito[j][0].lower():
                    carrito[j][2] = carrito[j][2] +1
                    duplicado = True
                    print(f'\n* Producto "{carrito[j][0]}" agregado al carrito')
            #si no esta en el carrito, agregarlo al carrito con una cantidad inicial
            if not duplicado:
                for i in range(len(productos)):
                    if agregar == productos[i][0].lower():
                        existe = True
                        print(f'\n* Producto "{productos[i][0]}" agregado al carrito')
                        name, price = productos[i]
                        lista_temporal = [name, price, 1]
                        carrito.append(lista_temporal)
            if not existe:
                print(f'\n*** No tenemos en stock el producto: "{agregar}" ***\n')
        elif opcion == 2:
            print('\n\nCarrito:')
            print(''.rjust(29,"="))
            if len(carrito)>=1:
                
                print('PRODUCTO'.rjust(20),'PRECIO'.rjust(20),'CANTIDAD'.rjust(20))
                print('--------'.rjust(20),'------'.rjust(20),'--------'.rjust(20))
                for i in range(len(carrito)):
                    print('*',f'{carrito[i][0]}'.center(28),f'S/{carrito[i][1]} c/u'.rjust(11),f'{carrito[i][2]}'.rjust(16))
                
        elif opcion == 3:
            if len(carrito)<=0:
                print('Tu carrito esta vacio. No procede')
            else:
                print('\n\nResumen de compra:')
                print(''.rjust(29,"="))
                debe = 0
                for i in range(len(carrito)):
                    nombre, precio, cantidad = carrito[i]
                    debe = (precio*cantidad)+debe
                #Mostrar su deuda
                print('PRODUCTO'.rjust(20),'PRECIO'.rjust(20),'CANTIDAD'.rjust(20))
                print('--------'.rjust(20),'------'.rjust(20),'--------'.rjust(20))
                # nombre precio cantidad total
                for i in range(len(carrito)):
                    print('*',f'{carrito[i][0]}'.center(28),f'S/ {carrito[i][1]} c/u'.rjust(11),f'{carrito[i][2]}'.rjust(16))
                print(f'|=> Total: S/{debe}')

                paga = float(input('¿Con cuanto pagaras? '))
                if paga<debe:
                    print(f'\n*** Con S/{paga} no cubre su cuenta de S/{debe} ***\n')
                elif paga==debe:
                    print(f'\n* No requiere cambio.\n** Gracias por su compra.\n')
                    break
                else:
                    #cambio
                    cambio = 0
                    cambio = paga - debe
                    print(f'\n* Tiene cambio de S/ {cambio}.\n** Gracias por su compra.\n')
                    break
                
        elif opcion == 4:
            print('\nSaliendo...\n')
            break
        else:
            print(f'\nNo existe la opcion {opcion}\n')
    except ValueError:
        print(f'\nNo existe esa opcion\n')
    except Exception as e:
        print(f'\n¡Error!: {e}\n')
    #else:
    #    print(f'\n¡AIR!\n')
    