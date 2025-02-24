import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime

def generar_informe(espacio, turnos):
    riqueza_por_turno = []
    riqueza_por_genero = defaultdict(list)
    riqueza_por_edad = defaultdict(list)

    for turno in range(turnos):
        riqueza_total_turno = sum(persona.monedas for persona in espacio.personas)
        riqueza_por_turno.append(riqueza_total_turno)
        
        for persona in espacio.personas:
            riqueza_por_genero[persona.sexo].append(persona.monedas)
            edad = datetime.now().year - persona.año_nacimiento
            riqueza_por_edad[edad].append(persona.monedas)

    # Gráfico de evolución de la riqueza
    plt.figure(figsize=(10, 5))
    plt.plot(range(turnos), riqueza_por_turno, marker='o')
    plt.title('Evolución de la riqueza total por turno')
    plt.xlabel('Turno')
    plt.ylabel('Riqueza total')
    plt.grid(True)
    plt.savefig('evolucion_riqueza.png')
    plt.show()

    # Gráfico de riqueza según género
    plt.figure(figsize=(10, 5))
    for genero, riquezas in riqueza_por_genero.items():
        plt.plot(range(turnos), riquezas, marker='o', label=genero)
    plt.title('Riqueza según género')
    plt.xlabel('Turno')
    plt.ylabel('Riqueza')
    plt.legend()
    plt.grid(True)
    plt.savefig('riqueza_genero.png')
    plt.show()

    # Gráfico de riqueza según edad
    plt.figure(figsize=(10, 5))
    for edad, riquezas in riqueza_por_edad.items():
        plt.plot(range(turnos), riquezas, marker='o', label=f'{edad} años')
    plt.title('Riqueza según edad')
    plt.xlabel('Turno')
    plt.ylabel('Riqueza')
    plt.legend()
    plt.grid(True)
    plt.savefig('riqueza_edad.png')
    plt.show()
