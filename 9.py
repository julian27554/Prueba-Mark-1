
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
    
    

    
    
