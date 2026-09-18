# conversiones.py

# Tasa de cambio fija para las conversiones de moneda.
# 1 USD = 18.50 MXN
TASA_USD_MXN = 18.50


def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def kilometros_a_millas(kilometros):
    return kilometros * 0.621371


def millas_a_kilometros(millas):
    return millas * 1.609344


def pesos_a_dolares(pesos):
    return pesos / TASA_USD_MXN


def dolares_a_pesos(dolares):
    return dolares * TASA_USD_MXN