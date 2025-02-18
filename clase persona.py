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
        if self.mes_nacimiento >=2:
            return 2024 - self.año_nacimiento
        else:
            return 2025 - self.año_nacimiento
    
    def saludar(self):
        return "Hola, soy " + self.nombre + " y tengo " + str(self.calcular_edad_en_años()) + " años"
    
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

    def recoger_moneda(self):
        self.monedas += 1
        return f"{self.nombre} ha recogido una moneda. Ahora tiene {self.monedas} monedas."

    def contar_monedas(self):
        return f"{self.nombre} tiene {self.monedas} monedas."

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

    def agregar_moneda(self, moneda):
        self.monedas.append(moneda)
        return f"Una moneda ha sido añadida al espacio {self.nombre}"

    def repartir_monedas(self):
        for persona in self.personas:
            if self.monedas:
                persona.recoger_moneda()
                self.monedas.pop()
            else:
                break
        return f"Se han repartido monedas en el espacio {self.nombre}"

class Moneda:
    def __init__(self, valor=1):
        self.valor = valor

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
        accion = input("¿Desea agregar una persona (a), listar personas (l), agregar moneda (m), repartir monedas (r) o salir (s)? ").lower()
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
        elif accion == 'm':
            moneda = Moneda()
            print(espacio.agregar_moneda(moneda))
        elif accion == 'r':
            print(espacio.repartir_monedas())
        else:
            print("Opción no válida. Por favor, elija 'a', 'l', 'm', 'r' o 's'.")
