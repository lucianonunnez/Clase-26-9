from operaciones import sumar,restar,costo_producto,ganancia_max



cantidad_mayo = int(input("Ingrese la cantidad vendida en Mayo: "))
cantidad_junio = int(input("Ingrese la cantidad vendida en Junio: "))
precio = float(input("Ingrese el precio unitario: "))

cantidad_vendida = sumar(cantidad_mayo,cantidad_junio)
dif_mensual = restar(cantidad_junio,cantidad_mayo)
costo_mayo = costo_producto(cantidad_mayo,precio)
costo_junio = costo_producto(cantidad_junio,precio)
ganancia_mayo = ganancia_max (cantidad_mayo,precio,costo_mayo)
ganancia_junio = ganancia_max (cantidad_junio,precio,costo_junio)
ganancia_total = sumar (ganancia_mayo,ganancia_junio)

print("La cantidad vendida en total es: ", cantidad_vendida)
print(f"En Junio se vendieron {dif_mensual} unidades por arriba de mayo")
print("El costo de los productos de mayo fue:",costo_mayo)
print("El costo de los productos de junio fue: ",costo_junio)
print("La ganancia total fue de: ",ganancia_total)