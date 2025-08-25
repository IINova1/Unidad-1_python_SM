from django.shortcuts import render

def inicio(request):
    contexto = {"nombre": "Sebita"}
    productos = [
        {"nombre": "Sensor 1", "Valor": 100},
        {"nombre": "Sensor 2", "Valor": 200},
        {"nombre": "Sensor 3", "Valor": 300}
    ]

    return render(request, "dispositivos/inicio.html", {
        "contexto": contexto,
        "productos": productos
    })
def panel_dispositivos(request):
    dispositivos = [
        {"nombre": "sensor temperatura", "consumo": 50},
        {"nombre": "medidor solar", "consumo": 120},
        {"nombre": "sensor movimiento", "consumo": 30},
        {"nombre": "calefactor", "consumo": 200}
    ]
    
    consumo_maximo = 100

    return render(request, "dispositivos/panel.html", {
        "dispositivos": dispositivos,
        "consumo_maximo": consumo_maximo
    })