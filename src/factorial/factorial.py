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

import sys


def factorial(num): 
    num1=int(input(f"ingrese el minimo del rango"))
    num2=int(input(f"ingrese el maximo del rango"))
    if (num < 0 and num1 < 0): 
        print("Factorial de un número negativo no existe o esta fuera de rango")

    elif num1 == 0 and num2==0: 
        return 1
        
    else: 
        lista=[]
        for i in range(num1, num2+1):
            lista.append(i)
            
            for num in lista:
                fact = 1
                
                while(num > 1): 
                    fact *= num 
                    num -= 1

                    
            print ("Factorial de" , i ," ,", fact)


if len(sys.argv) == 0:
   print("Debe informar un número!")
   sys.exit()
num=int(sys.argv[1])
factorial(num) 
 






