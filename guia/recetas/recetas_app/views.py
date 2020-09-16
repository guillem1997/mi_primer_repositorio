from django.shortcuts import render
def Home_view(request):
    return render(request, 'Home.html')
def Menú_Infantil_view(request):
    return render(request, 'Menú_Infantil.html')
def Receta_Facil_view(request):
    return render(request, 'Receta_Facil.html')
def Mafe_view(request):
    return render(request, 'Mafe.html')
def Feijoada_view(request):
    return render(request, 'Feijoada.html')
def Pizza_view(request):
    return render(request, 'Pizza.html')
def Canelones_view(request):
    return render(request, 'Canelones.html')
def Flor_de_Calabacin_view(request):
    return render(request, 'Flor_de_Calabacin.html')
def Gazpacho_view(request):
    return render(request, 'Gazpacho.html')
def Sopa_de_Noodles_view(request):
    return render(request, 'Sopa_de_Noodles.html')
def Ensaladilla_Rusa_view(request):
    return render(request, 'Ensaladilla_Rusa.html')
def Carbonara_view(request):
    return render(request, 'Carbonara.html')

# Create your views here.
