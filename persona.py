import math
import random

class Persona:
    def __init__(self, nombre, año_nacimiento, mes_nacimiento, dia_nacimiento, lugar_nacimiento, sexo):
        self.nombre = nombre
        self.año_nacimiento = año_nacimiento
        self.mes_nacimiento = mes_nacimiento
        self.dia_nacimiento = dia_nacimiento
        self.lugar_nacimiento = lugar_nacimiento
        self.sexo = sexo
        self.x = 0
        self.y = 0
        self.monedas = 0
        
    def calcular_edad_en_años(self):
        if self.mes_nacimiento >= 2:
            return 2024 - self.año_nacimiento
        else:
            return 2025 - self.año_nacimiento
    
    def saludar(self):
        return "Hola, soy " + self.nombre + "y tengo " + str(self.calcular_edad_en_años()) + " años"
    
    def calcular_edad_en_meses(self):
        edad_en_meses = self.calcular_edad_en_años() * 12 + (self.mes_nacimiento - 2)
        return f"Tengo {edad_en_meses} meses"
    
    def calcular_edad_en_dias(self):
        edad_en_meses = self.calcular_edad_en_años() * 12 + (self.mes_nacimiento - 2)
        edad_en_dias = edad_en_meses * 30
        return f"Tengo {edad_en_dias} días"
    
    def mover_a(self, nueva_x, nueva_y):
        self.x = nueva_x
        self.y = nueva_y
        return f"Me he movido a la nueva ubicación: ({self.x}, {self.y})"

    def agregar_monedas(self, cantidad):
        self.monedas += cantidad
        return f"{self.nombre} ahora tiene {self.monedas} monedas"

class Espacio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.personas = []
        self.monedas = []

    def agregar_persona(self, persona):
        self.personas.append(persona)
        return f"{persona.nombre} ha sido añadido al espacio {self.nombre}"

    def listar_personas(self):
        if not self.personas:
            return f"No hay personas en el espacio {self.nombre}"
        return f"Personas en el espacio {self.nombre}: " + ", ".join([persona.nombre for persona in self.personas])

    def repartir_monedas(self, cantidad):
        for persona in self.personas:
            monedas_a_repartir = random.randint(1, cantidad)
            persona.agregar_monedas(monedas_a_repartir)
            cantidad -= monedas_a_repartir
            if cantidad <= 0:
                break
        return f"Se han repartido monedas en el espacio {self.nombre}"
    
def calcular_distancia(persona1, persona2):
    return math.sqrt((persona1.x - persona2.x) ** 2 + (persona1.y - persona2.y) ** 2)

def estan_en_misma_posicion(persona1, persona2):
    return persona1.x == persona2.x and persona1.y == persona2.y

def contar_personas_en_espacio(espacio):
    return len(espacio.personas)

if __name__ == "__main__":
    nombre_espacio = input("Ingrese el nombre del espacio: ")
    espacio = Espacio(nombre_espacio)
    
    while True:
        accion = input("¿Desea agregar una persona (a) o listar personas (l) o salir (s)? ").lower()
        if accion == 's':
            break
        elif accion == 'a':
            nombre = input("Ingrese el nombre de la persona: ")
            año_nacimiento = int(input("Ingrese el año de nacimiento: "))
            mes_nacimiento = int(input("Ingrese el mes de nacimiento: "))
            dia_nacimiento = int(input("Ingrese el día de nacimiento: "))
            lugar_nacimiento = input("Ingrese el lugar de nacimiento: ")
            sexo = input("Ingrese el sexo: ")
            persona = Persona(nombre, año_nacimiento, mes_nacimiento, dia_nacimiento, lugar_nacimiento, sexo)
            print(espacio.agregar_persona(persona))
        elif accion == 'l':
            print(espacio.listar_personas())
        else:
            print("Opción no válida. Por favor, elija 'a', 'l' o 's'.")

class Moneda:
    def __init__(self, valor):
        self.valor = valor

def mover_todas_las_personas(espacio):
    for persona in espacio.personas:
        nueva_x = random.randint(0, 100)
        nueva_y = random.randint(0, 100)
        persona.mover_a(nueva_x, nueva_y)

def persona_recoge_moneda(persona, espacio):
    for moneda in espacio.monedas:
        if persona.x == moneda.x and persona.y == moneda.y:
            persona.agregar_monedas(moneda.valor)
            espacio.monedas.remove(moneda)
            return f"{persona.nombre} ha recogido una moneda de valor {moneda.valor}"
    return f"{persona.nombre} no ha encontrado ninguna moneda"

def cuantas_monedas_tiene_persona(persona):
    return persona.monedas

def riqueza_total(espacio):
    total = sum(persona.monedas for persona in espacio.personas)
    return total

def combate(persona1, persona2):
    if persona1.x == persona2.x and persona1.y == persona2.y:
        ganador = random.choice([persona1, persona2])
        perdedor = persona2 if ganador == persona1 else persona1
        ganador.monedas += perdedor.monedas
        perdedor.monedas = 0
        return f"{ganador.nombre} ha ganado el combate y ahora tiene {ganador.monedas} monedas"
    return "Las personas no están en la misma posición para combatir"

persona = Persona("Juan", 1990, 5, 15, "Lima", "M")
print(persona.saludar())
print(persona.calcular_edad_en_meses())
print(persona.calcular_edad_en_dias())
print(persona.mover_a(10, 20))
print(persona.agregar_monedas(15))