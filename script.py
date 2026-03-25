#!/usr/bin/env python3

# Aufgabe: Programmieren Sie einen einfachen Taschenrechner

# Ihr Taschenrechner soll folgende Funktionen unterstützen:
# - Addition (+)
# - Subtraktion (-)
# - Multiplikation (*)
# - Division (/)

# Der Benutzer sollte aufgefordert werden, zwei Zahlen einzugeben.
# Anschließend sollte der Benutzer die gewünschte Operation wählen können.

# Beispielablauf:
# 1. Benutzer gibt die erste Zahl ein.
# 2. Benutzer gibt die zweite Zahl ein.
# 3. Benutzer wählt die Operation (+, -, *, /).
# 4. Das Programm führt die Berechnung durch und gibt das Ergebnis aus.

# Optional: Erweitern Sie den Taschenrechner um weitere Funktionen wie Potenzierung oder Modulo.
# Variablen

#addition
from re import match
import sys
from unittest import case


def addieren(x, y):
    return x + y
# Subtraktion
def subtrahieren(x, y):
    return x - y
# Multiplikation
def multiplizieren(a, b):
  return a * b

# Division
def dividieren(a, b):
    return a / b

#Modulo
def rest_berechnen(a, b):
    return a % b

# Potenzierung
def potenzieren(a, b):
    return a ** b

# Abfrage der Operation
def operation_abfrage(zahl_1, operation, zahl_2):
    match operation:
        case "+":
            return addieren(zahl_1, zahl_2)
        case "-":
            return subtrahieren(zahl_1, zahl_2)
        case "*":
            return multiplizieren(zahl_1, zahl_2)
        case "/":
            return dividieren(zahl_1, zahl_2)
        case "%":
            return rest_berechnen(zahl_1, zahl_2)
        case "**":
            return potenzieren(zahl_1, zahl_2)
        case _:
            print("Ungültige Operation")
            return None

# Abfrage der Zahlen und Operation
def eingabe_abfrage():
    zahl_1 = float(input("Bitte geben Sie die erste Zahl ein: "))
    operation = input("Bitte wählen Sie die gewünschte Operation (+, -, *, /, %, **): ")
    zahl_2 = float(input("Bitte geben Sie die zweite Zahl ein: "))
    return zahl_1, operation, zahl_2

# Hauptprogramm
zahl_1, operation, zahl_2 = eingabe_abfrage()
ergebnis = operation_abfrage(zahl_1, operation, zahl_2)

if ergebnis is None: 
    print("Keine Berechnung durchgeführt.")
else : print("Das Ergebnis der Berechnung ist:", ergebnis)

sys.exit()
