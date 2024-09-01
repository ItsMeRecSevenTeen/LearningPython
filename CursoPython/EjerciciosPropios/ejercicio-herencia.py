class Animal:
    def animal(self, nombre):
        self.nombre = nombre

    def hablar(self):
        raise NotImplementedError("Subclase debe implementar el método 'hablar'.")


class Perro(Animal):
    def hablar(self):
        return "¡Guau!"


class Gato(Animal):
    def hablar(self):
        return "¡Miau!"


# Crear instancias de las clases derivadas
perro = Perro()
perro.animal("Bobby")

gato = Gato()
gato.animal("Mimi")


# Llamar al método hablar en cada instancia
print(perro.nombre + ": " + perro.hablar())  # Bobby: ¡Guau!
print(gato.nombre + ": " + gato.hablar())  # Mimi: ¡Miau!
