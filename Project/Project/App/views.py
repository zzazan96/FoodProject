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
            #모든 값이 작성되지 않을시 에러표시
        else:
            User = get_object_or_404(Usertbl,userid=userID)
            #페이지에서 받아온 userID값과 같은 userid값을 가진 객체를 db의 Usertbl에서 불러와 User객체에 저장.같은 값이 없으면 404에러 호출 
            if check_password(userpassword, User.userpassword):
            #페이지에서 받아온 비밀번호와 User객체의 비밀번호가 일치한지 검사
                user_code = User.usercode
                #User객체의 usercode(pk)를 user_code에 할당
                request.session['user'] = user_code
                #user를 키로하고 값을 user_code로 하는 세션 설정
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
    #세션이 존재하면 세션을 제거하여 로그아웃
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

def listview(request):  
    return render(request, 'webApp/listview.html')
    