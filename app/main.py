from fastapi import FastAPI
from .conversor import celsius_a_fahrenheit, fahrenheit_a_celsius, km_a_millas, millas_a_km

app = FastAPI(title="Conversor CI")

@app.get("/")
def root():
    return {"message": "Bienvenido al conversor de unidades"}

@app.get("/celsius-to-fahrenheit/{celsius}")
def api_celsius_a_fahrenheit(celsius: float):
    return {"fahrenheit": celsius_a_fahrenheit(celsius)}

@app.get("/fahrenheit-to-celsius/{fahrenheit}")
def api_fahrenheit_a_celsius(fahrenheit: float):
    return {"celsius": fahrenheit_a_celsius(fahrenheit)}

@app.get("/km-to-miles/{km}")
def api_km_a_millas(km: float):
    return {"miles": km_a_millas(km)}

@app.get("/miles-to-km/{miles}")
def api_millas_a_km(miles: float):
    return {"km": millas_a_km(miles)}
