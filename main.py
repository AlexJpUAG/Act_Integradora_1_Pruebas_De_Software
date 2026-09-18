# main.py

import conversiones


def mostrar_menu():
    print("\n=== CONVERSOR DE UNIDADES ===")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Kilómetros a Millas")
    print("4. Millas a Kilómetros")
    print("5. Pesos Mexicanos a Dólares")
    print("6. Dólares a Pesos Mexicanos")
    print("0. Salir")


def main():

    while True:

        mostrar_menu()

        opcion = input("Selecciona una opción: ")

        if opcion == "0":
            print("Programa terminado.")
            break

        if opcion not in ["1", "2", "3", "4", "5", "6"]:
            print("Opción no válida.")
            continue

        try:
            valor = float(input("Ingresa el valor numérico: "))

        except ValueError:
            print("Error: debes ingresar un valor numérico.")
            continue

        if opcion == "1":
            resultado = conversiones.celsius_a_fahrenheit(valor)
            print(f"{valor:.2f} °C = {resultado:.2f} °F")

        elif opcion == "2":
            resultado = conversiones.fahrenheit_a_celsius(valor)
            print(f"{valor:.2f} °F = {resultado:.2f} °C")

        elif opcion == "3":
            resultado = conversiones.kilometros_a_millas(valor)
            print(f"{valor:.2f} km = {resultado:.2f} millas")

        elif opcion == "4":
            resultado = conversiones.millas_a_kilometros(valor)
            print(f"{valor:.2f} millas = {resultado:.2f} km")

        elif opcion == "5":
            resultado = conversiones.pesos_a_dolares(valor)
            print(f"${valor:.2f} MXN = ${resultado:.2f} USD")

        elif opcion == "6":
            resultado = conversiones.dolares_a_pesos(valor)
            print(f"${valor:.2f} USD = ${resultado:.2f} MXN")


if __name__ == "__main__":
    main()