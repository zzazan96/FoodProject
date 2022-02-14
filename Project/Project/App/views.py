from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import get_object_or_404
from .models import Ingredienttbl
from .models import Usertbl
from .models import Recipetbl
from .models import Listtbl
from .models import List2tbl
from .models import List3tbl
from .models import Cooktbl
from .models import Recipeingredienttbl


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
    Lists = Listtbl.objects.all()
    return render(request, 'webApp/save.html', {'Lists': Lists})

def save2(request):
    Lists = List2tbl.objects.all()
    return render(request, 'webApp/save2.html', {'Lists': Lists})

def save3(request):
    Lists = List3tbl.objects.all()
    return render(request, 'webApp/save3.html', {'Lists': Lists})
       
def savefix(request): 
    Lists = Listtbl.objects.all()
    if request.method == 'GET':
        return render(request, 'webApp/savefix.html', {'Lists': Lists})
    elif request.method == 'POST':
        listid = request.POST.get('pk',None)
        volume = request.POST.get('p_num1',None)
        fixlist = Listtbl.objects.get(listid=listid)
        fixlist.volume = volume
        fixlist.save()
        return render(request, 'webApp/savefix.html', {'Lists': Lists})
    
def search(request):
    Ingredients = Ingredienttbl.objects.all()
    return render(request, 'webApp/search.html', {'Ingredients':Ingredients})

def Userlist(request):
    return render(request, 'webApp/Userlist.html')

def Ulist1(request):
    recipe = Recipetbl.objects.get(recipeid=1)
    return render(request, 'webApp/Ulist1.html', {'recipe':recipe})

def Ulist2(request):
    recipe = Recipetbl.objects.get(recipeid=1)
    return render(request, 'webApp/Ulist2.html', {'recipe':recipe})

def Ulist3(request):
    recipe = Recipetbl.objects.get(recipeid=1)
    return render(request, 'webApp/Ulist3.html', {'recipe':recipe})

def listsave(request):
    return render(request, 'webApp/listsave.html')

def mainlist(request):    
    Recipes = Recipetbl.objects.all()
    return render(request, 'webApp/mainlist.html', {'Recipes':Recipes})

def mlist1(request):
    recipe = Recipetbl.objects.get(recipeid=1)
    return render(request, 'webApp/mlist1.html', {'recipe':recipe})

def mlist2(request):
    recipe = Recipetbl.objects.get(recipeid=2)  
    return render(request, 'webApp/mlist2.html', {'recipe':recipe})

def mlist3(request):
    recipe = Recipetbl.objects.get(recipeid=3)  
    return render(request, 'webApp/mlist3.html', {'recipe':recipe})

def mlist4(request):
    recipe = Recipetbl.objects.get(recipeid=4)  
    return render(request, 'webApp/mlist4.html', {'recipe':recipe})

def mlist5(request):
    recipe = Recipetbl.objects.get(recipeid=5)  
    return render(request, 'webApp/mlist5.html', {'recipe':recipe})

def mlist6(request):
    recipe = Recipetbl.objects.get(recipeid=6)  
    return render(request, 'webApp/mlist6.html', {'recipe':recipe})

def mlist7(request):
    recipe = Recipetbl.objects.get(recipeid=7)  
    return render(request, 'webApp/mlist7.html', {'recipe':recipe})

def mlist8(request):
    recipe = Recipetbl.objects.get(recipeid=8)  
    return render(request, 'webApp/mlist8.html', {'recipe':recipe})

def cook(request):
    if request.method == 'GET':         
        return render(request, 'webApp/cook.html')
    elif request.method == 'POST':
        Recipes = Cooktbl.objects.all()
        return render(request, 'webApp/cook.html', {'Recipes':Recipes})

def Clist1(request):
    recipe = Cooktbl.objects.get(recipeid=1)  
    return render(request, 'webApp/Clist1.html', {'recipe':recipe})

def Clist2(request):
    recipe = Cooktbl.objects.get(recipeid=2)  
    return render(request, 'webApp/Clist2.html', {'recipe':recipe})

def Clist3(request):
    recipe = Cooktbl.objects.get(recipeid=3)  
    return render(request, 'webApp/Clist3.html', {'recipe':recipe})

def Clist4(request):
    recipe = Cooktbl.objects.get(recipeid=4)  
    return render(request, 'webApp/Clist4.html', {'recipe':recipe})

def searchplus(request):
    return render(request, 'webApp/searchplus.html')
    