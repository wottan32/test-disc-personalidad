# Define las constantes para cada categoría del test
DOMINANTE = "dominante"
INFLUYENTE = "influyente"
SUBMISIVO = "submisivo"
CONCIENTE = "conciente"

# Crea un diccionario para almacenar las puntuaciones de cada categoría
puntuaciones = {
    DOMINANTE: 0,
    INFLUYENTE: 0,
    SUBMISIVO: 0,
    CONCIENTE: 0
}

# Pregunta al usuario que responda a cada pregunta del test
# y suma la puntuación a la categoría correspondiente
pregunta1 = input("¿Te gusta liderar a otros? (s/n)")
if pregunta1 == "s":
    puntuaciones[DOMINANTE] += 1

pregunta2 = input("¿Te gusta persuadir a otros para que hagan lo que quieres? (s/n)")
if pregunta2 == "s":
    puntuaciones[INFLUYENTE] += 1

pregunta3 = input("¿Te gusta seguir las reglas y evitar conflictos? (s/n)")
if pregunta3 == "s":
    puntuaciones[SUBMISIVO] += 1

pregunta4 = input("¿Te gusta planificar y ser organizado? (s/n)")
if pregunta4 == "s":
    puntuaciones[CONCIENTE] += 1

pregunta5 = input("¿Te gusta asumir riesgos y tomar decisiones importantes? (s/n)")
if pregunta5 == "s":
    puntuaciones[DOMINANTE] += 1

pregunta6 = input("¿Te gusta trabajar con otros y hacer que se sientan cómodos? (s/n)")
if pregunta6 == "s":
    puntuaciones[INFLUYENTE] += 1

pregunta7 = input("¿Te gusta trabajar solo y evitar llamar la atención? (s/n)")
if pregunta7 == "s":
    puntuaciones[SUBMISIVO] += 1

pregunta8 = input("¿Te gusta ser preciso y atenerte a los detalles? (s/n)")
if pregunta8 == "s":
    puntuaciones[CONCIENTE] += 1

pregunta9 = input("¿Te gusta competir y ganar? (s/n)")
if pregunta9 == "s":
    puntuaciones[DOMINANTE] += 1

pregunta10 = input("¿Te gusta ser el centro de atención y hacer reír a los demás? (s/n)")
if pregunta10 == "s":
    puntuaciones[INFLUYENTE] += 1

pregunta11 = input("¿Te gusta ser discreto y no llamar la atención? (s/n)")
if pregunta11 == "s":
    puntuaciones[SUBMISIVO] += 1

pregunta12 = input("¿Te gusta ser preciso y atenerte a los detalles? (s/n)")
if pregunta12 == "s":
    puntuaciones[CONCIENTE] += 1

pregunta13 = input("¿Te gusta tomar el control y ser el jefe? (s/n)")
if pregunta13 == "s":
    puntuaciones[DOMINANTE] += 1

pregunta14 = input("¿Te gusta ser el mediador y resolver conflictos? (s/n)")
if pregunta14 == "s":
    puntuaciones[INFLUYENTE] += 1

pregunta15 = input("¿Te gusta seguir las reglas y evitar problemas? (s/n)")
if pregunta15 == "s":
    puntuaciones[SUBMISIVO] += 1

pregunta16 = input("¿Te gusta planificar y ser organizado? (s/n)")
if pregunta16 == "s":
    puntuaciones[CONCIENTE] += 1

pregunta17 = input("¿Te gusta tomar el control y ser el jefe? (s/n)")
if pregunta17 == "s":
    puntuaciones[DOMINANTE] += 1

pregunta18 = input("¿Te gusta ser el mediador y resolver conflictos? (s/n)")
if pregunta18 == "s":
    puntuaciones[INFLUYENTE] += 1

pregunta19 = input("¿Te gusta seguir las reglas y evitar problemas? (s/n)")
if pregunta19 == "s":
    puntuaciones[SUBMISIVO] += 1

pregunta20 = input("¿Te gusta tomar el control y ser el jefe? (s/n)")
if pregunta20 == "s":
    puntuaciones[DOMINANTE] += 1

pregunta21 = input("¿Te gusta persuadir a otros para que hagan lo que quieres? (s/n)")
if pregunta21 == "s":
    puntuaciones[INFLUYENTE] += 1

pregunta22 = input("¿Te gusta trabajar solo y evitar llamar la atención? (s/n)")
if pregunta22 == "s":
    puntuaciones[SUBMISIVO] += 1

pregunta23 = input("¿Te gusta ser preciso y atenerte a los detalles? (s/n)")
if pregunta23 == "s":
    puntuaciones[CONCIENTE] += 1

pregunta24 = input("¿Te gusta asumir riesgos y tomar decisiones importantes? (s/n)")
if pregunta24 == "s":
    puntuaciones[DOMINANTE] += 1

pregunta25 = input("¿Te gusta trabajar con otros y hacer que se sientan cómodos? (s/n)")
if pregunta25 == "s":
    puntuaciones[INFLUYENTE] += 1

# Imprime las puntuaciones finales
print("Puntuaciones:")
for categoria, puntuacion in puntuaciones.items():
    print(f"{categoria}: {puntuacion}")





"""
    Dominante (D): Las personas dominantes son decididas, independientes y seguras de sí mismas. Les gusta tomar el control y ser el líder. Son proactivas y no les importa asumir riesgos para alcanzar sus metas.

    Influyente (I): Las personas influyentes son sociales, comunicativas y persuasivas. Les gusta persuadir a otros para que hagan lo que quieren y son buenas en hacer que se sientan cómodos y a gusto. Disfrutan estando en el centro de atención y trabajan bien en equipo.

    Submisivo (S): Las personas submisivas son pacientes, cooperativas y leales. Les gusta seguir las reglas y evitar conflictos, y son buenas en resolver problemas y mantener la armonía en un grupo. Son dependientes y les gusta trabajar en equipo.

    Conciente (C): Las personas concientes son precisas, detallistas y organizadas. Les gusta planificar y ser organizadas y son buenas en seguir las instrucciones y trabajar de manera sistemática. Son reflexivas y les gusta pensar antes de actuar.
"""