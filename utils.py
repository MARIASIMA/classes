import random

def mover_todas_las_personas(espacio):
    for persona in espacio.personas:
        nueva_x = random.randint(0, 100)
        nueva_y = random.randint(0, 100)
        persona.mover_a(nueva_x, nueva_y)
    return "Todas las personas han sido movidas a nuevas posiciones."

def persona_recoge_moneda(espacio):
    for persona in espacio.personas:
        for moneda in espacio.monedas:
            if persona.x == moneda.x and persona.y == moneda.y:
                persona.agregar_monedas(moneda.valor)
                espacio.monedas.remove(moneda)
                break
    return "Las personas han recogido las monedas en sus posiciones."

def cuantas_monedas_tiene_persona(persona):
    return f"{persona.nombre} tiene {persona.monedas} monedas."

def riqueza_total(espacio):
    total_monedas = sum(persona.monedas for persona in espacio.personas)
    return f"La riqueza total en el espacio {espacio.nombre} es de {total_monedas} monedas."

def combate(persona1, persona2):
    if persona1.x == persona2.x and persona1.y == persona2.y:
        ganador = random.choice([persona1, persona2])
        perdedor = persona1 if ganador == persona2 else persona2
        ganador.agregar_monedas(perdedor.monedas)
        perdedor.monedas = 0
        return f"{ganador.nombre} ha ganado el combate y ahora tiene {ganador.monedas} monedas. {perdedor.nombre} ha perdido todas sus monedas."
    return "Las personas no están en la misma posición, no hay combate."
