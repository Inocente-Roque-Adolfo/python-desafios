#Proyecto 01 - Adivina el número secreto
#Juego interactivo 
""" #El programa seleccionara aleatoriamente un número entre un rango
#especifico y el jugador debera adivinar el 'número secreto' en 
#un número limitado de intentos """

from random import randrange

lim_inferior, lim_superior, cant_Intentos = 1,100,2
numero_secreto = randrange(lim_inferior,lim_superior)
print('\nBienvenido a "Adivina el Número Secreto"'.center(52),'\n','========================================'.rjust(45),f'\n\nHe seleccionado un número entre {lim_inferior} y {lim_superior}. ¡Adivina cual es!')
try:
    for intento in range(cant_Intentos):
        consumir = 0
        while consumir!=1:
            while consumir !=1:
                try:
                    print(f'Intento {intento+1}/{cant_Intentos}')
                    apuesta = int(input('Ingresa tu adivinanza: '))
                    break
                except ValueError:
                    print('\nSolo se adivina números enteros\n')
                    consumir = 1
                except Exception as e:
                    print(f'\nSucedio un ERROR: {e}\n')
            if consumir!=1:
                if apuesta<lim_inferior or apuesta>lim_superior:
                    print(f'\n**¡FALLO! El rango es de {lim_inferior}-{lim_superior}\n')
                    consumir = 1
                else:
                    break
        if consumir!=1:
            if numero_secreto>apuesta:
                print('===========================El número secreto es mayor\n')
            elif numero_secreto<apuesta:
                print('===========================El número secreto es menor\n')
            else:
                plural = ['intento' if intento==0 else 'intentos']
                print(f'\n¡Felicidades! Adivinazte el numero secreto {apuesta} en {intento+1} {plural[0]}\n')
                break
    if numero_secreto!=apuesta:
        print(f'\nLo siento, el numero secreto era {numero_secreto}. ¡no te rindas!\n')
except Exception as e:
    print(f'\nSucedio un ERROR: {e}\n')