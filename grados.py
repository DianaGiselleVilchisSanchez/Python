def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def mostrar_menu():
    print("Conversor de Temperaturas")
    print("1. Convertir Celsius a Fahrenheit")
    print("2. Convertir Fahrenheit a Celsius")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            celsius = float(input("Introduce la temperatura en Celsius: "))
            fahrenheit = celsius_a_fahrenheit(celsius)
            print(f"{celsius}°C son {fahrenheit}°F")

        elif opcion == '2':
            fahrenheit = float(input("Introduce la temperatura en Fahrenheit: "))
            celsius = fahrenheit_a_celsius(fahrenheit)
            print(f"{fahrenheit}°F son {celsius}°C")

        elif opcion == '3':
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
