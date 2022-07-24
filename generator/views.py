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

    length = int(request.GET.get('length'))
    uppercase = request.GET.get('uppercase')
    specialCharacters = request.GET.get('specialCharacters')
    numbers = request.GET.get('numbers')

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

    ranges = {
        'password': generate_password,
    }

    template = 'index.html'
    return render(request, template, ranges)