#Proyecto 05 - Conversor de un número romano a número entero
#
#Programa que permita convertir un número romano a su equivalente en números enteros
#Especificaciones:
#EI programa deberá solicitar al usuario que ingrese un número romano
#El programa aceptara números romanos en un rango entre 1 y 3999.
#PRIMERA FORMA

while True:
    romano = input('Ingrese el numero en romanos: ').upper()
    letras = list(romano) #C C C X C I V
    letras.reverse()    #V I C X C C C 
    
    #M>D>C>L>X>I
    basicosRomanos = {"M":1000,"D":500,'C':100,'L':50,'X':10,'V':5,'I':1}
    
    existe = 0
    valor_actual = 0
    valor_anterior = 0
    num_entero = 0
    #No procede si no existe alguna de las letras en romanos
    temporal_conjunto = set(letras)
    keys = set(list(basicosRomanos.keys()))
    resta = temporal_conjunto - keys 

    if len(resta)==0:
        #Cambiar la lista por sus valores numericos
        for indice in range(len(letras)):
            for letter, value in basicosRomanos.items():
                if letras[indice] == letter:
                    letras[indice]=value
        #print(letras)
        """
        #RETO ADICIONAL 
        #No se pueden usar más de tres símbolos iguales seguidos 
        #después de una cifra mayor

        #ni más de un símbolo a la izquierda de una cifra mayor

        lista_3 = []
        for i in range(len(letras)):
            cantidad = letras.count(letras[i])
            print(cantidad)
        """
        

        #Sumar o restas 
        for values in letras:
            valor_actual = values
            if valor_anterior<=valor_actual:
                num_entero = num_entero + valor_actual
                #print('SUMA',num_entero)
            else:
                num_entero = num_entero - valor_actual
                #print('RESTA',num_entero)
            valor_anterior=valor_actual
        print('\nRomano: ',romano)
        print('Arábigo: ',num_entero,'\n')
    else:
        print('No se reconoce como numeros romanos\n')

#REGLA
#if P1 > P2
#    P1 - P2
#else:
#   P1 + P2