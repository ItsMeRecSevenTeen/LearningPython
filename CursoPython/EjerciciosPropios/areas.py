import math


def area_del_circulo(radio):
    area = math.pi * (float(radio) ** 2)
    return f"El area del circulo es: {area}"


def area_del_rectangulo(lado, ancho):
    area = int(lado) * int(ancho)
    return f"El area del rectangulo es: {area}"


def area_del_triangulo(base, altura):
    area = (int(base) * int(altura)) / 2
    return f"El area del triangulo es: {area}"


def area_de_esfera(radio):
    area = (4 * math.pi) * (float(radio) ** 2)
    return f"El area de la esfera es: {area}"


respuesta = ""

while respuesta.lower() != "x":
    respuesta = input(
        """Que area deseas calcular? (Escribe el numero de opcion) Si deseas salir, ingresa 'x'
1.- Area del circulo        2.- Area del rectangulo         3.- Area del Triangulo
4.- Area de la esfera\n"""
    )
    if respuesta == "1":
        respuesta = input("Dame el radio de tu circulo: ")
        print(area_del_circulo(respuesta))
    elif respuesta == "2":
        respuesta = input("Dame el lado de tu rectangulo: ")
        anch = input("Dame el ancho de tu rectangulo: ")
        print(area_del_rectangulo(respuesta, anch))
    elif respuesta == "3":
        respuesta = input("Dame la base de tu triangulo: ")
        alt = input("Dame la altura de tu triangulo: ")
        print(area_del_triangulo(respuesta, alt))
    elif respuesta == "4":
        respuesta = input("Dame el radio de tu esfera: ")
        print(area_de_esfera(respuesta))
    else:
        print("Opcion invalida, Intenta de nuevo\n")
