from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Ingredienttbl
from .models import Usertbl
from .models import Recipetbl

def login(request):
    if request.method == 'GET':
        return render(request, 'webApp/login.html')
    elif request.method == 'POST':
        userID = request.POST.get('userid', None)
        userpassword = request.POST.get('userpassword', None)
        res_data = {}
        if not (userID and userpassword):
            res_data['error'] = '모든 값을 입력해주세요.'
        else:
            User = get_object_or_404(Usertbl,userid=userID)
            if check_password(userpassword, User.userpassword):
                user_code = User.usercode
                request.session['user'] = user_code
                return redirect('mainlist')
            else:
                res_data['error'] = '잘못된 아이디 또는 비밀번호입니다.'
        return render(request, 'webApp/login.html', res_data)
                
def register(request):  
    if request.method == 'GET':
        return render(request, 'webApp/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        userID = request.POST.get('userID', None)
        password = request.POST.get('password', None)   
        passwordconfirm = request.POST.get('passwordconfirm', None)           

        res_data = {}
        
        if password != passwordconfirm:
            res_data['error'] = '비밀번호가 일치하지 않습니다.'
        else:
            user = Usertbl(
                username=username,
                useremail=useremail,
                userid=userID,
                userpassword=make_password(password)
            )
            user.save()
        
        return render(request, 'webApp/register.html', res_data)
        
def logout(request):
    if request.session.get('user'):
        del request.session['user']
    return redirect('/')

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

def list(request):  
    return render(request, 'webApp/list.html')

def list2(request):  
    return render(request, 'webApp/list2.html')
    