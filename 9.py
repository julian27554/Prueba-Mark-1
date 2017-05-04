#Introduccion a la programacion
#Desarrollo de taller de programacion

#Problema: restar la parte decimal a la parte entera

#Entradas: numero de 3 digitos enteros y 3 digitos decimales(float)

#Salidas: sustraccion de la parte decimal y entera

#Restricciones: numero >0 y <1000


#Procedimientos:

#1| ingresar el numero
#2| convertir a entero
#3| modular la cifra por 10
#4| dividir la cifra entera y modular
#5| repetir ciclo para los caracteres
#6| multiplicar cifra inicial por 1000
#7| convertir a entero
#8| modular la cantidad
#9| divir por entero y modular todo entre 10
#10| dividir por entero 100 y modular por 10
#11| restar parte entera a parte decimal
#12| encontrar respuesta
#13| imprimir resultado 

def operador_1(val):

    entero=int(val)

    
    tercera_cifra_entera=entero%10
    segunda_cifra_entera=(entero//10)%10
    primera_cifra_entera=entero//100

    Z=tercera_cifra_entera+segunda_cifra_entera+primera_cifra_entera


    
    decimal=int(val*1000)

    tercera_cifra_decimal=decimal%10
    segunda_cifra_decimal=(decimal//10)%10
    primera_cifra_decimal=(decimal//100)%10

    D1=tercera_cifra_decimal+segunda_cifra_decimal+primera_cifra_decimal


    R1=Z-D1
    
    return R1
    
    

    
    
