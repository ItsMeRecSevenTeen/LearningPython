numeros = [2, 4, 5, 1, 9, 1]
# numeros.sort(reverse=True)
numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

usuarios = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)
