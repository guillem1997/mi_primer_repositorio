from django.shortcuts import render
from django.http import HttpResponse
import psycopg2


def home(request):
    return render(request, 'home.html')


def anadir(request):
    prioridad = request.POST["name_prioridad"]
    titulo = request.POST["name_titulo"]
    nota = request.POST["name_nota"]
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO nota VALUES ('{prioridad}','{titulo}','{nota}');")
    conn.commit()
    cursor.close()
    conn.close()
    return render(request, 'home.html')
# Create your views here.
