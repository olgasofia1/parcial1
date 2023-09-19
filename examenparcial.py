totalsA=float(adultos)*25 
totalsN=float(niños)*20
totals=float(totalsA)+float(totalsN)
print("Este es el total en pesos de sillas:",totals)
mesaA=float(adultos)*17
print("El total en pesos de mesa de adultos:",mesaA)
mesaN=float(niños)*17
print("El total en pesos de mesa de niño",mesaN)
cuantasmesasA=float(mesaA)/170
cuantasmesasN=float(mesaN)/170
totaldecarpas=float(cuantasmesasA)+float(cuantasmesasN)
pesocarpa=float(totaldecarpas)*630
print("El total de carpas en pesos son:",pesocarpa)
subtotal=float(pesocarpa)+float(mesaA)+float(mesaN)
print("El subtotal es",subtotal)
impuestos=float(subtotal)*0.16
print("Cantidad de impuestos",impuestos)
impuestostotal=float(subtotal)+float(impuestos) #
print("Total con impuestos",impuestostotal)
print("De cuanto es tu descuento:")
descuento=input()
descuentoenpesos=float(impuestostotal)*float(descuento)/100
print("Cantidad de descuento en pesos:",descuentoenpesos)
total=float(impuestostotal)-float(descuentoenpesos)
print("total con descuento",total)
