from django.shortcuts import render
# Import the models you want to use
from .models import Dispositivo, Medicion 

def inicio(request):
    # This view remains the same for now.
    Dispositivos = Dispositivo.objects.select_related('categoria')
    return render(request, "dispositivos/inicio.html", {"dispositivos": Dispositivos})
def panel_dispositivos(request):
    # 1. Get all 'Dispositivo' objects from the database.
    todos_los_dispositivos = Dispositivo.objects.all()
    
    # 2. You can also get other data, for example, the latest measurements.
    ultimas_mediciones = Medicion.objects.order_by('-timestamp')[:5] # Get the 5 most recent

    # 3. Pass the real data to the template.
    contexto = {
        "dispositivos": todos_los_dispositivos,
        "mediciones": ultimas_mediciones,
    }

    return render(request, "dispositivos/panel.html", contexto)

def crear_dispositivo(request):
    if request.method == 'POST':
        form = dispositivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Listar dipositivos')  # Redirect to the device panel after creation
    else:
        form = dispositivoForm()
    
    return render(request, 'dispositivos/crear.html', {'form': form})