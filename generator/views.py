import random
import string
from django.shortcuts import render
from django.http import JsonResponse
from zxcvbn import zxcvbn  # Para evaluar seguridad de la contraseña
from passlib.hash import bcrypt  # Para cifrar contraseñas



def generar_contrasena(longitud=12, incluir_mayus=True, incluir_numeros=True, incluir_simbolos=True, excluir=""):
    """ Genera una contraseña segura según los criterios proporcionados """

    caracteres = string.ascii_lowercase  # Minúsculas por defecto
    if incluir_mayus:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    # Excluir caracteres específicos
    caracteres = ''.join([c for c in caracteres if c not in excluir])

    # Generar la contraseña aleatoria
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def api_generar_contrasena(request):
    """ API que genera una contraseña y devuelve la seguridad en formato JSON """
    if request.method == "GET":
        longitud = int(request.GET.get('longitud', 12))
        incluir_mayus = request.GET.get('incluir_mayus', 'true') == 'true'
        incluir_numeros = request.GET.get('incluir_numeros', 'true') == 'true'
        incluir_simbolos = request.GET.get('incluir_simbolos', 'true') == 'true'
        excluir = request.GET.get('excluir', '')

        # Generar contraseña
        contrasena = generar_contrasena(longitud, incluir_mayus, incluir_numeros, incluir_simbolos, excluir)

        # Evaluar seguridad
        seguridad = zxcvbn(contrasena)['score']  # Devuelve de 0 (débil) a 4 (muy fuerte)

        return JsonResponse({
            'contrasena': contrasena,
            'seguridad': seguridad,
            'mensaje': evaluar_nivel_seguridad(seguridad)
        })

def evaluar_nivel_seguridad(nivel):
    """ Retorna un mensaje según el nivel de seguridad """
    mensajes = {
        0: "Contraseña muy débil 🚨",
        1: "Contraseña débil ⚠️",
        2: "Contraseña moderada 🟡",
        3: "Contraseña fuerte ✅",
        4: "Contraseña muy fuerte 🔒"
    }
    return mensajes.get(nivel, "Desconocido")


    
def home(request):
    """ Página principal con el formulario de generación de contraseñas """
    if request.method == "POST":
        longitud = int(request.POST.get('longitud', 12))
        incluir_mayus = 'incluir_mayusculas' in request.POST
        incluir_numeros = 'incluir_numeros' in request.POST
        incluir_simbolos = 'incluir_simbolos' in request.POST

        # Generar contraseña
        contrasena = generar_contrasena(longitud, incluir_mayus, incluir_numeros, incluir_simbolos)

        # Evaluar seguridad
        seguridad = zxcvbn(contrasena)['score']
        nivel_seguridad = evaluar_nivel_seguridad(seguridad)

        return render(request, 'generator/home.html', {
            'contrasena': contrasena,
            'seguridad': nivel_seguridad
        })

    return render(request, 'generator/home.html')

