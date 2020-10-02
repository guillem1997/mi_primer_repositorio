from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import psycopg2.extras

import psycopg2


def home(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")

    cursor = conn.cursor()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    prioridad = request.GET.get('get_prioridad', default=None)
    if (prioridad is None):
        cursor.execute(f"SELECT * FROM Nota;")
    else:
        cursor.execute(f"SELECT * FROM Nota WHERE prioridad='{prioridad}';")
    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()

    params = {'notas': result}
    return render(request, 'home.html', params)


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
    return redirect('/home')


def consultar(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")
    cursor = conn.cursor()
    cursor.execute("select * from nota")
    html = '<html><a href="http://127.0.0.1:8000/home">Home</a> <br>'
    columns = [col[0] for col in cursor.description]
    for column in columns:
        html += str(column) + '|'
    html += '<br>'
    for nota in cursor.fetchall():
        for columna in nota:
            html += str(columna) + '|'
        html += '<br>'
    html += '</html>'
    cursor.close()
    conn.close()
    return HttpResponse(html)


def borrar(request):
    conn = psycopg2.connect(dbname="capitulo_6_db",
                            user="capitulo_6_user",
                            password="patata")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM nota")
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/home')
# Create your views here.
