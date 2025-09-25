from fastapi import FastAPI
from app.conversor import celsius_a_fahrenheit, fahrenheit_a_celsius, km_a_millas, millas_a_km

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Bienvenido al conversor de unidades"}


@app.get("/celsius-to-fahrenheit/{c}")
def api_celsius_to_fahrenheit(c: float):
    return {"fahrenheit": celsius_a_fahrenheit(c)}


@app.get("/fahrenheit-to-celsius/{f}")
def api_fahrenheit_to_celsius(f: float):
    return {"celsius": fahrenheit_a_celsius(f)}


@app.get("/km-to-miles/{km}")
def api_km_to_miles(km: float):
    return {"miles": km_a_millas(km)}


@app.get("/miles-to-km/{miles}")
def api_miles_to_km(miles: float):
    return {"km": millas_a_km(miles)}
