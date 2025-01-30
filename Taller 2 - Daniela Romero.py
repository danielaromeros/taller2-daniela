#Taller 2 - Trabajo en Parejas

import random

#Esta función selecciona aleatoriamente tres líneas y genera un haiku cada vez que se ejecuta.

def generate_haiku():
    five_syllables = [
        "Brisa en la montaña",
        "Luz de luna suave",
        "Cantan los grillos",
        "Vuela mariposa",
        "Noche estrellada"
    ]
    
    seven_syllables = [
        "El río fluye sin fin",
        "Las hojas caen despacio",
        "El sol brilla en el lago",
        "Sopla el viento en los campos",
        "Las olas besan la orilla"
    ]
    
    haiku = f"{random.choice(five_syllables)}\n{random.choice(seven_syllables)}\n{random.choice(five_syllables)}"
    return haiku

print(generate_haiku())