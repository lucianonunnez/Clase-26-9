from operaciones2 import costo_total,costo_aberturas

ambientes = int(input("Ingrese la cantidad de ambientes: "))
puertas = int(input("Ingrese la cantidad de puertas: "))
ventanas = int(input("Ingrese la cantidad de ventanas: "))
ventanal = int(input("Ingrese la cantidad de ventanales: "))
madera = float(input("Ingrese el precio de la madera x m2: "))

costo_puertas = costo_aberturas(puertas,madera)
costo_ventanas = costo_aberturas(ventanas,madera)
costo_ventanal = costo_aberturas(ventanal,madera)
total = costo_total (costo_puertas,costo_ventanas,costo_ventanal,ambientes)

print("Costo de las puertas",costo_puertas)
print("Costo de las ventanas", costo_ventanas)
print("Costo de los ventanales", costo_ventanal)
print("Costo total de las aberturas", total)



# operaciones2.py
"""
def costo_aberturas (aberturas,madera):
    
    total = aberturas*madera*1.6

    return total

def costo_total (puertas,ventanas,ventanal,ambientes):
    
    total = puertas*ventanas*ventanal*ambientes

    return total


"""