from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from .models import Ingredienttbl
from .models import Usertbl
# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request,'webApp/login.html')
    elif request.method == 'POST':
        userid = request.POST.get('userID',None)
        userpassword = request.POST.get('userpassword',None)
        
        res_data = {}
        if not (userid and userpassword):
            res_data['error']="모든 칸을 입력해주세요."
        else:
            usertbl = Usertbl.objects.get(userid = userid)
        
            if check_password(userpassword, usertbl.userpassword):
                return render(request, 'webApp/mainlist.html')
            else:
                res_data['error'] = "비밀번호가 틀렸습니다."
        return render(request, 'webApp/login.html', res_data)

def logout(request):
    logout(request)
    return render('webApp/login.html')

def save(request):
    return render(request, 'webApp/save.html')

def savefix(request):
    return render(request, 'webApp/savefix.html')

def search(request):
    Ingredients = Ingredienttbl.objects.all()
    context = {'Ingredients':Ingredients}
    return render(request, 'webApp/search.html', context)

def Userlist(request):
    return render(request, 'webApp/Userlist.html')

def mainlist(request):
    return render(request, 'webApp/mainlist.html')

def listsave(request):
    return render(request, 'webApp/listsave.html')

def register(request):  
    if request.method == 'GET':
        return render(request, 'webApp/register.html')
    
    elif request.method == 'POST':
        print(request.POST)
        username = request.POST.get('userName',None)
        useremail = request.POST.get('userEmail',None)
        userid = request.POST.get('userID',None)
        userpassword = request.POST.get('userPassword',None)
        userpassword_confirm = request.POST.get('userPasswordConfirm',None)
            
        res_data = {}  
        if(username or useremail or userpassword) == '':
            res_data['error'] = "모든 값을 입력해야 합니다."
        elif userpassword != userpassword_confirm:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            usertbl = Usertbl(
                username = username,
                useremail = useremail,
                userpassword = make_password(userpassword),
                userid = userid
            )
            usertbl.save()
                
        return render(request, 'webApp/register.html', res_data)
    