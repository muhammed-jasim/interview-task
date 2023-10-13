# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup,name='signup'),
    path('login/',views.Loginn,name='login'),
    path('terms&condition',views.Terms,name='terms&condition'),
    path('logout',views.logout,name='logout'),
    path('index',views.Index,name='index'),
    path('navbar',views.Navbar,name='navbar'),
    path('add_employee',views.addemployee,name='addemployee'),
    path('employeelist',views.employee_list,name='employeelist'),
    path('delete_employee<int:i>',views.employee_dlt,name='delete_employee'),
    path('empupdate<int:i>',views.update,name='empupdate'),
    path('empdoupdate',views.emp_doupdate,name='empdoupdate')
]