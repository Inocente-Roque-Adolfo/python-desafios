#Proyecto 04 - Conversor de un número entero a número romano
#
#Programa que permita convertir un número entero a su equivalente en números romanos
#Especificaciones:
#EI programa deberá solicitar al usuario que ingrese un número entero
#El programa aceptara números enteros en un rango entre 1 y 3999.
#PRIMERA FORMA
while True:
    try:
        numero = int(input('\n\nIngrese un numero: '))
        if numero>0 and numero<4000:
            unidades = numero%10
            decenas = (numero//10)%10
            centenas = ((numero//10)//10)%10
            millar = ((numero//10)//10)//10
            #print(millar,centenas,decenas,unidades)
            print('Número en romanos: ', end='')
            #imprimir los millare
            if millar>=1 and millar<=3:
                for i in range(millar):
                    print('M', end='')

            #imprimir las centenas
            if centenas>=1 and centenas<=3:
                for i in range(centenas):
                    print('C', end='')
            elif centenas>=5 and centenas<=8:
                centenas_nuevas = centenas-5
                print('D', end='')
                for i in range(centenas_nuevas):
                    print('C', end='')
            elif centenas==4:
                print('CD', end='')
            elif centenas==9:
                print('CM', end='')
            #else:
            #    print('ES CERO LAS CENTENAS')

            #imprimir las decenas
            if decenas>=1 and decenas<=3:
                for i in range(decenas):
                    print('X', end='')
            elif decenas>=5 and decenas<=8:
                decenas_nuevas = decenas-5
                print('L', end='')
                for i in range(decenas_nuevas):
                    print('X', end='')
            elif decenas==4:
                print('XL', end='')
            elif decenas==9:
                print('XC', end='')
            #else:
            #    print('ES CERO LAS DECENAS')

            #imprimir las unidades
            if unidades>=1 and unidades<=3:
                for i in range(unidades):
                    print('I', end='')
            elif unidades>=5 and unidades<=8:
                unidades_nuevas=unidades-5
                print('V', end='')
                for i in range(unidades_nuevas):
                    print('I', end='')
            elif unidades==4:
                print('IV', end='')
            elif unidades==9:
                print('IX', end='')
            #else:
            #    print('ES CERO LA UNIDAD')
        else:
            print('Rango es de 1-3999')
    except ValueError:
        print('No ingrese letras ni caracteres')
    except Exception as e:
        print('¡Error!: {e}')

"""
#SEGUNDA FORMA
try:
    num = int(input('Ingresa un número entero: '))
    if 1<=num<=3999:
        M = ['','M','MM','MMM']
        C = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        D = ['','X','XX','XXX','LX','L','LX','LXX','LXXX','XC']
        U = ['','I','II','III','IV','V','VI','VII','VIII','IX']
        print(f"{M[num//1000]}{C[(num%1000)//100]}{D[(num%100)//10]}{U[num%10]}")
except ValueError:
        print('No ingrese letras ni caracteres')
except Exception as e:
    print(f'¡Error!: {e}')
"""