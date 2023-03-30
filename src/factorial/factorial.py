#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Gonzalez Claudio                                                        *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
#import sys
#def factorial(num): 
#    if num < 0: 
#        print("Factorial de un número negativo no existe")

    #elif num == 0: 
    #    return 1
        
#    else: 
#        fact = 1
#        while(num > 1): 
#            fact *= num 
#            num -= 1
#        return fact 

#if len(sys.argv) == 0:
#   print("Debe informar un número!")
#   sys.exit()
#num=int(sys.argv[1])
#print("Factorial ",num,"! es ", factorial(num)) 


#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un rango de numeros                             *
#* Gonzalez Claudio                                                        *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*

#Modifique el argumento (y el ingreso manual) para aceptar números en el rango
#desde-hasta (ej. 4-8) y que calcule los factoriales entre ambos extremos.

#import sys


#def factorial(num): 
#    num1=int(input(f"ingrese el minimo del rango"))
#    num2=int(input(f"ingrese el maximo del rango"))
#    if (num < 0 and num1 < 0): 
#        print("Factorial de un número negativo no existe o esta fuera de rango")

#    elif num1 == 0 and num2==0: 
#        return 1
        
#    else: 
#        lista=[]
#        for i in range(num1, num2+1):
#            lista.append(i)
            
#            for num in lista:
#                fact = 1
                
#                while(num > 1): 
#                    fact *= num 
#                    num -= 1

                    
#            print ("Factorial de" , i ," ,", fact)


#if len(sys.argv) == 0:
#   print("Debe informar un número!")
#   sys.exit()
#num=int(sys.argv[1])
#factorial(num) 
 

#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial desde- hasta                                       *
#* Gonzalez Claudio                                                        *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*

#Modifique el argumento (y el ingreso manual) para que acepte rangos sin límite
#inferior “-hasta” calculando entre 1 y el número indicado (ejemplo “-10”), lo
#mismo para “desde-“ calculando entre el número indicado y 60

import sys


def factorial(num): 
    hasta=int(input(f"ingrese hasta que numero"))
    desde=int(input(f"ingrese desde que numero"))
    if (num < 0 and hasta < 0): 
        print("Factorial de un número negativo no existe o esta fuera de rango")

    elif hasta == 0 and desde==0: 
        return 1
        
    else: 
        lista_hasta=[]
        lista_desde=[]
        for i in range(1, hasta+1):
            lista_hasta.append(i)
                 
            for num in lista_hasta:
                fact = 1
                
                while(num > 1): 
                    fact *= num 
                    num -= 1

                    
            print ("Factorial de" , i ," ,", fact)

        for i in range(desde,61):
            lista_desde.append(i)

            for num in lista_desde:
                fact = 1

                while(num > 1):
                    fact *= num
                    num -= 1

            print("factorial de" , i ,",", fact )


if len(sys.argv) == 0:
   print("Debe informar un número!")
   sys.exit()
num=int(sys.argv[1])
factorial(num) 

