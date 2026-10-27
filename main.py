
from unittest import result

from pyscript import document

non_metals = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.003),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904)
}


def verify_nonmetal(event):
    Element1 = document.getElementById("symbol").value.strip().capitalize()

    result = non_metals.get(Element1, ("Element not found", "-", "-"))

    if result[0] == "Element not found":
        document.getElementById("result").innerText = (
            "Element does not exist in the non-metals list."
        )
    else:
        document.getElementById("result").innerHTML = (
            f"Element Symbol: {Element1}<br>"
            f"Element Name: {result[0]}<br>"
            f"Atomic Number: {result[1]}<br>"
            f"Atomic Mass: {result[2]}"
        )

        