from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'webApp/main.html')

def mainfix(request):
    return render(request, 'webApp/mainfix.html')

def search(request):
    return render(request, 'webApp/search.html')

def Userlist(request):
    return render(request, 'webApp/Userlist.html')

def list(request):
    return render(request, 'webApp/list.html')

def listsave(request):
    return render(request, 'webApp/listsave.html')