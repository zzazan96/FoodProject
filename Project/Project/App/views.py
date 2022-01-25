from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'webApp/login.html')

def save(request):
    return render(request, 'webApp/save.html')

def savefix(request):
    return render(request, 'webApp/savefix.html')

def search(request):
    return render(request, 'webApp/search.html')

def Userlist(request):
    return render(request, 'webApp/Userlist.html')

def mainlist(request):
    return render(request, 'webApp/mainlist.html')

def listsave(request):
    return render(request, 'webApp/listsave.html')

def register(request):
    return render(request, 'webApp/register.html')    