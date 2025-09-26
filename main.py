import operaciones 

cantidad = 100
precio = 500

a = operaciones.sumar(cantidad,precio)
b = operaciones.restar(cantidad,precio)
costo = operaciones.costo_producto(cantidad,precio)
d = operaciones.ganancia_max (cantidad,precio,costo)

print(a,b,costo,d)