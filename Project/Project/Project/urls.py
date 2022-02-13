"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login, name='login'),
    path('logout/', views.logout, name="logout"),
    path('save/', views.save, name='save'),
    path('Userlist/', views.Userlist, name='Userlist'),
    path('Userlist/listsave/', views.listsave, name='listsave'),
    path('save/search/', views.search, name='search'),
    path('save/search/searchplus/', views.searchplus, name='searchplus'),
    path('save/savefix/', views.savefix, name='savefix'),
    path('mainlist/',views.mainlist, name='mainlist'),
    path('mainlist/mlist1/',views.mlist1, name='mlist1'),
    path('mainlist/mlist2/',views.mlist2, name='mlist2'),
    path('mainlist/mlist3/',views.mlist3, name='mlist3'),
    path('mainlist/mlist4/',views.mlist4, name='mlist4'),
    path('mainlist/mlist5/',views.mlist5, name='mlist5'),
    path('mainlist/mlist6/',views.mlist6, name='mlist6'),
    path('mainlist/mlist7/',views.mlist7, name='mlist7'),
    path('mainlist/mlist8/',views.mlist8, name='mlist8'),
    path('Userlist/Ulist1/',views.Ulist1, name='Ulist1'),
    path('Userlist/Ulist2/',views.Ulist2, name='Ulist2'),
    path('Userlist/Ulist3/',views.Ulist3, name='Ulist3'),
    path('register/',views.register, name='register'),
    path('cook/',views.cook, name='cook'),
    path('cook/Clist1/',views.Clist1, name='Clist1'),
    path('cook/Clist2/',views.Clist2, name='Clist2'),
    path('cook/Clist3/',views.Clist3, name='Clist3'),
    path('cook/Clist4/',views.Clist4, name='Clist4'),

]
