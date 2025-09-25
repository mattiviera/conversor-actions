def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def km_a_millas(km):
    return km * 0.621371


def millas_a_km(millas):
    return millas / 0.621371


if __name__ == "__main__":
    print("25°C a Fahrenheit:", celsius_a_fahrenheit(25))
    print("77°F a Celsius:", fahrenheit_a_celsius(77))
    print("10 km a millas:", km_a_millas(10))
    print("6.2 millas a km:", millas_a_km(6.2))
