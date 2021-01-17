from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return HttpResponse('<h1>hello friend!</h1>')

def about(request):
    return render(request, 'generator/aboutpage.html')

def mainpage(request):
    return render(request, 'generator/mainpage.html', {'password':'gqwfieqfqg', 'user':'Harshith'})


def eggs(request):
    return HttpResponse('Eggs are so good')

def passwor(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length',12))
    thepassword = ''

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        thepassword += random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        length -= 1

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
        thepassword += random.choice(list('1234567890'))
        length -= 1

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
        thepassword += random.choice(list('!@#$%^&*()'))
        length -= 1


    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})
