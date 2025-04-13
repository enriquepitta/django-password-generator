from ast import If
from email import charset
from lib2to3.pgen2.pgen import generate_grammar
from random import random
from re import template
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def about(request):
    template = 'about.html'
    return render(request, template)

def home(request):
    template = 'index.html'
    return render(request, template)

def password(request):
    length = int(request.GET.get('length', 12))  # Valor por defecto 12 si no se selecciona

    # Obtener si están marcados o no
    uppercase = 'uppercase' in request.GET
    specialCharacters = 'specialCharacters' in request.GET
    numbers = 'numbers' in request.GET

    character = list('abcdefghijklmnñopqrstuvwxyz')
    generate_password = ''

    if uppercase:
        character.extend(list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"))

    if specialCharacters:
        character.extend(list("°|!#$%&/()=?¡¿´+-*<>"))

    if numbers:
        character.extend(list("0123456789"))

    for _ in range(length):
        generate_password += random.choice(character)

    # Este diccionario pasa todos los valores necesarios al template
    context = {
        'password': generate_password,
        'length': length,
        'uppercase': uppercase,
        'specialCharacters': specialCharacters,
        'numbers': numbers,
    }

    return render(request, 'index.html', context)