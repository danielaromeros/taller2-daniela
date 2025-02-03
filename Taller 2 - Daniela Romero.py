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

def roll_dice(sides=6):
    return random.randint(1, sides)
print(f"Dado: {roll_dice()}")


print("\n\U0001F3B2 Bienvenido al juego de Adivina el Número! \U0001F3B2")
print("Estoy pensando en un número entre 1 y 100...")

# Elige un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    try:
        # Pide al usuario que ingrese un número
        adivinanza = int(input("\n¡Adivina el número!: "))
        intentos += 1

        if adivinanza < numero_secreto:
            print("Demasiado bajo. 🔻 Intenta de nuevo.")
        elif adivinanza > numero_secreto:
            print("Demasiado alto. 🔺 Intenta de nuevo.")
        else:
            print(f"\n✨ ¡Felicitaciones! Adivinaste el número {numero_secreto} en {intentos} intentos. 🎉")
            break
    except ValueError:
        print("Por favor, ingresa un número válido. 😅")

#cambio de cami
def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

# Solicitar al usuario que ingrese un año
anio = int(input("Ingresa un año: "))

# Verificar si el año es bisiesto
if es_bisiesto(anio):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")