from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Ingredienttbl
from .models import Usertbl
from .models import Recipetbl
# Create your views here.

def login(request):
    return render(request, 'webApp/login.html')

def logout(request):
    logout(request)
    return render('webApp/login.html')

def save(request):
    return render(request, 'webApp/save.html')

def savefix(request):
    return render(request, 'webApp/savefix.html')

def search(request):
    Ingredients = Ingredienttbl.objects.all()
    return render(request, 'webApp/search.html', {'Ingredients':Ingredients})

def Userlist(request):
    return render(request, 'webApp/Userlist.html')

def mainlist(request):
    Recipes = Recipetbl.objects.all()
    return render(request, 'webApp/mainlist.html', {'Recipes':Recipes})

def listsave(request):
    return render(request, 'webApp/listsave.html')

def register(request):  
    return render(request, 'webApp/register.html')

def listview(request):  
    return render(request, 'webApp/listview.html')
    