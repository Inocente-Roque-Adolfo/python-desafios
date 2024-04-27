#Proyecyo 03 - Piensa un número
#Juego interactivo 
""""
#El usuario debe ser invitado a pensar en un número secreto, y el
programa intentará adivinarlo haciendo preguntas astutas
"""
#importacion de solo randrange del modulo random con el alias aleatorio 
from random import randrange as aleatorio

#Inicializacion de los limites
lim_inferior, lim_superior = 1,100
#Impresion de las condiciones del proyecto

print(f'\n\nPiensa en un número del ({lim_inferior}-{lim_superior}). Trataré de adivinarlo.')
print(''.center(53,'='))
#Inicializacion de las variables
lim_superior+=1
intento = 0
#Para que no cambie de numero le pedimos el numero pensado
"""
#Para que funcione descomenta lineas abajo, donde hay un comentario de varias lineas 
#Repetir si surge la excepcion hasta q nos de el numero 
while True:
    try:
        #Repetir hasta que el numero este en el rango
        while True:
            tu_numero = int(input('Tu numero: '))
            if tu_numero>=lim_inferior and tu_numero<lim_superior:
                break
            else:
                print(f'Un número del ({lim_inferior}-{lim_superior-1})\n')
        break
    except ValueError:
        print(f'Un número del ({lim_inferior}-{lim_superior-1})\n')
"""

#for intento in range(lim_inferior,lim_superior):
while True:
    #resetear para q no mantega el valor en la siguiente iteracion
    omitir = ''
    #Genera en cada iteracion un numero aleatorio
    #Los limites varian en cada iteracion
    apuesta = aleatorio(lim_inferior,lim_superior)
    
    """
    ###ADICIONAL
    #Si el dato random es igual al numero del usuario:
    if apuesta==tu_numero:
        #imprime automatico 
        plural_singular = ['s' if intento!=0 else '']
        #al intento se le reduce 1 porque el ultimo iterable no se considera un intento por ser la unica opcion 
        print('\n',f'¡Adivine! tu número ({apuesta}) en {intento} intento{plural_singular[0]}'.rjust(48),'\n')
        break
    """
    #Condicional por descarte el ultima opcion posible
    #Cuando se encuentre entre dos limites, donde solo puede ser 1 digito
    if len(range(lim_inferior,lim_superior))==1:
        #imprime automatico 
        plural_singular = ['s' if intento!=0 else '']
        #al intento se le reduce 1 porque el ultimo iterable no se considera un intento por ser la unica opcion 
        print('\n',f'¡Adivine! tu número ({apuesta}) en {intento} intento{plural_singular[0]}'.rjust(48),'\n')
        break

    #Imprimer la lista con los datos que pueden ser el numero del usuario
    #print(f"\nEntoy entre: {list(range(lim_inferior,lim_superior))}")
    #Mostramos el numero aleatorio asignado
    print('\n\n',f'¿Es {apuesta} tu número?'.center(40, '-').rjust(45))

##Las opciones idoneas para que no de error
    #Si el dato aleatorio es igual al limite inferior
    #No puede retroceder porque apuesta es el primer dato de las opciones a escoger
    if apuesta==lim_inferior:
        #mensaje personalizado sin menor porque no puede ir hacia atras 
        mensaje = '"mayor"'
        #opcion a ignorar y resetear el bucle si lo ingresa
        omitir ='menor'
    #Si el dato aleatorio coincide con el limite superior menos 1
    #No puede avanzar porque apuesta es el ultimo dato de las opciones a escoger
    elif apuesta==lim_superior-1:
        #mensaje personalizado sin mayor porque no puede ir hacia adelante 
        mensaje = '"menor"'
        #opcion a ignorar y resetear el bucle si lo ingresa
        omitir = 'mayor'
    else:
        #Si no hay restricciones mostrar todas las opciones
        mensaje = '"menor" | "mayor"'

    #para que ingrese una opcion, con un mensaje personalizado, convertimos en minuscula para comparativas
    ayuda = input(f'Opciones: {mensaje} | "correcto":  '.rjust(48)).lower()
    
    #Si coincide lo que ingresa el usuario con lo que se debe omitir, retorna al inicio del bucle
    if ayuda==omitir:
        #mensaje de error
        print('\n','**Ingresa solo una de las opciones'.rjust(42))
        #omite lo que continua y va al inicio del bucle
        continue

##Las condicionales solo suceden si lo que ingresa el usuario es diferente a lo que se debe omitir
    #Si el usuario indica que su numero es menor
    if ayuda=='menor':
        #El limite superior del siguiente ramdom sera el numero ramdom actual propuesto (apuesta)
        lim_superior = apuesta
    #Si el usuario indica que su numero es mayor
    elif ayuda=='mayor':
        #El limite inferior del siguiente ramdom sera el numero ramdom actual propuesto aumentado en 1 (apuesta+1)
        #Para que no considera el suiguiente rango aleatorio el mismo numero random actual 
        lim_inferior = apuesta+1
    #Si el usuario indica que su numero es correcto
    elif ayuda=='correcto':
        #Si es  el primer intento la palabra (intentos) debe ir en singular
        plural_singular = ['intento' if intento==0 else 'intentos']
        #Se dice el numero adivinado y el intento
        print('\n',f'¡Adivine! tu número ({apuesta}) en {intento+1} {plural_singular[0]}'.rjust(48),'\n')
        #Se debe salir del bucle while cuando se adivine
        break
    #Si no coincide ninguna opcion
    else:
        #mensaje de error
        print('\n','**Ingresa solo una de las opciones'.rjust(42))
    
    #incremento los intentos para saber con cuantas se adivina
    intento+=1