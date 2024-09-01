mensaje = """Bienvenido a la calculadora ByR17,"""
print(mensaje)
conteo = 0
numero1 = input("Ingresa el primer numero: ")
operacion = input("Ingresa la operacion: ")
numero2 = input("Ingresa el segundo numero: ")
while (
    numero1.lower() != "salir"
    or operacion.lower() != "salir"
    or numero2.lower() != "salir"
):
    if conteo != 0:
        numero1 = input("Ingresa el primer numero: ")
        operacion = input("Ingresa la operacion: ")
        numero2 = input("Ingresa el segundo numero: ")

    if operacion.lower() == "sumar":
        respuesta = int(numero1) + int(numero2)
        print("El resultado de la suma es: ", respuesta)
        conteo += 1
    if operacion.lower() == "restar":
        respuesta = int(numero1) - int(numero2)
        print("El resultado de la resta es: ", respuesta)
        conteo += 1
    if operacion.lower() == "multiplicar":
        respuesta = int(numero1) * int(numero2)
        print("El resultado de la multiplicacion es: ", respuesta)
        conteo += 1
    if operacion.lower() == "dividir":
        respuesta = int(numero1) / int(numero2)
        print("El resultado de la division es: ", respuesta)
        conteo += 1
print("Saliendo")
