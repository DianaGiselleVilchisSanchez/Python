import random

def adivina_el_numero():
    numero_aleatorio = random.randint(1, 100)
    intentos = 0
    adivinanza = 0

    print("¡Bienvenido al juego de adivinar el número!")
    print("He elegido un número entre 1 y 100. ¡Intenta adivinarlo!")

  
    while adivinanza != numero_aleatorio:

        adivinanza = int(input("Introduce tu adivinanza: "))
        intentos += 1

        if adivinanza < numero_aleatorio:
            print("El número es mayor. Intenta de nuevo.")
        elif adivinanza > numero_aleatorio:
            print("El número es menor. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")

adivina_el_numero()
