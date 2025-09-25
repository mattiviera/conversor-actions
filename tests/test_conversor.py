from app.conversor import celsius_a_fahrenheit, fahrenheit_a_celsius, km_a_millas, millas_a_km


def test_celsius_a_fahrenheit():
    assert celsius_a_fahrenheit(0) == 32
    assert celsius_a_fahrenheit(100) == 212
    assert round(celsius_a_fahrenheit(-40), 2) == -40


def test_fahrenheit_a_celsius():
    assert fahrenheit_a_celsius(32) == 0
    assert fahrenheit_a_celsius(212) == 100
    assert round(fahrenheit_a_celsius(-40), 2) == -40


def test_km_a_millas():
    assert round(km_a_millas(1), 6) == 0.621371
    assert round(km_a_millas(10), 6) == 6.21371
    assert round(km_a_millas(0), 6) == 0


def test_millas_a_km():
    assert round(millas_a_km(1), 6) == 1.609344
    assert round(millas_a_km(6.21371), 5) == 10
    assert round(millas_a_km(0), 6) == 0
