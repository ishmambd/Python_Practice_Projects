# eng_unit_converter.py
"""
Engineering Unit Converter (CLI)
Convert between common engineering units (length, force, pressure, angle).

Shows:
    - Menus
    - Functions
    - Input validation
"""

from math import pi


def mm_to_m(value: float) -> float:
    return value / 1000.0


def m_to_mm(value: float) -> float:
    return value * 1000.0


def n_to_kn(value: float) -> float:
    return value / 1000.0


def kn_to_n(value: float) -> float:
    return value * 1000.0


def kpa_to_mpa(value: float) -> float:
    return value / 1000.0


def mpa_to_kpa(value: float) -> float:
    return value * 1000.0


def deg_to_rad(value: float) -> float:
    return value * pi / 180.0


def rad_to_deg(value: float) -> float:
    return value * 180.0 / pi


def c_to_k(value: float) -> float:
    return value + 273.15


def k_to_c(value: float) -> float:
    return value - 273.15


def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("[ERROR] Please enter a valid number.")


def converter_menu():
    print("\n=== Engineering Unit Converter ===")
    print("1.  mm  → m")
    print("2.  m   → mm")
    print("3.  N   → kN")
    print("4.  kN  → N")
    print("5.  kPa → MPa")
    print("6.  MPa → kPa")
    print("7.  deg → rad")
    print("8.  rad → deg")
    print("9.  °C  → K")
    print("10. K   → °C")
    print("0.  Exit")


def main():
    while True:
        converter_menu()
        choice = input("Select an option (0–10): ").strip()

        if choice == "0":
            print("Goodbye, engineer! 🏗")
            break

        if choice not in {str(i) for i in range(1, 11)}:
            print("[ERROR] Invalid option. Try again.")
            continue

        value = get_float("Enter value: ")

        if choice == "1":
            result = mm_to_m(value)
            print(f"{value} mm = {result} m")
        elif choice == "2":
            result = m_to_mm(value)
            print(f"{value} m = {result} mm")
        elif choice == "3":
            result = n_to_kn(value)
            print(f"{value} N = {result} kN")
        elif choice == "4":
            result = kn_to_n(value)
            print(f"{value} kN = {result} N")
        elif choice == "5":
            result = kpa_to_mpa(value)
            print(f"{value} kPa = {result} MPa")
        elif choice == "6":
            result = mpa_to_kpa(value)
            print(f"{value} MPa = {result} kPa")
        elif choice == "7":
            result = deg_to_rad(value)
            print(f"{value}° = {result} rad")
        elif choice == "8":
            result = rad_to_deg(value)
            print(f"{value} rad = {result}°")
        elif choice == "9":
            result = c_to_k(value)
            print(f"{value} °C = {result} K")
        elif choice == "10":
            result = k_to_c(value)
            print(f"{value} K = {result} °C")

        print()


if __name__ == "__main__":
    main()
