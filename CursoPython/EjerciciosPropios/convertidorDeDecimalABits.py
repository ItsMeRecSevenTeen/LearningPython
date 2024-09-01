def obtenerBinarioPositivo(numeroDecimal):
    cadena = str(bin(numeroDecimal))
    return cadena[2:]

def obtenerBinarioNegativo(numeroDecimal):
    cadena = str(bin(~numeroDecimal))
    return cadena[3:]

minimo = int(input("Ingresa el limite minimo del rango a calcular\n"))
maximo = int(input("Ingresa el limite maximo del rango a calcular\n"))

print("Decimal\tBinario Positivo\tBinario Negativo")
for x in range(minimo, maximo + 1):
    print(x, "\t\t", obtenerBinarioPositivo(x),"\t\t", obtenerBinarioNegativo(x))