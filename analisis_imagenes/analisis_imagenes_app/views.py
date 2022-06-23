from django.shortcuts import render


def home(request):
    return render(request, "analisis_imagenes_app/home.html", )

def servicios(request):

    return render(request, "gestion_sarlaft/servicios.html", )



# Create your views here.
