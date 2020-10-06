anyo = 2011     #Variable anyo con valor de 2011

#Definición año bisiesto:
#“Un año es bisiesto si es divisible entre 4, excepto el último de cada siglo
#aquel divisible por 100), salvo que sea divisible por 400.”

#Si año divisible entre 400 = SIEMPRE BISIESTO
#Si año divisible entre 4 y no entre 100 = BISIESTO
#Si año divisible entre 4 y entre 100 = NO BISIESTO

bisiesto = (anyo%400==0 or (anyo%4==0 and not anyo%100==0))     #CONDICIÓN BISIESTO (ÓPTIMA)

print (bisiesto)        #Imprimir valor de bisiesto (bool)