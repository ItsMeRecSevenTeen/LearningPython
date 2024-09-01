saludo = 25


def saludar():
    global saludo
    saludo = "Hola mundo"


def saludaChanchito():
    saludo = "Hola Chanchito"
    print(saludo)


resultado1 = saludo + 3
print(saludo)
saludar()
resultado2 = saludo + 3
print(saludo)
