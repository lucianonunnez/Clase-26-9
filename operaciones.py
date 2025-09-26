from math import sqrt,pi, exp

def sumar(a,b):
    sum = a+b
    return sum

def restar (a,b):
    resta = a-b
    return resta 

def costo_producto (cantidad,precio):
    
    costo = sqrt(cantidad)*precio*pi

    return costo

def ganancia_max (cantidad,precio,costo):

    ganancia_max = sqrt(cantidad)*precio*costo

    return ganancia_max