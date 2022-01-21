#for the forms to work we import these header files
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
# app_name ='bookstore'

urlpatterns =[
    path('', home, name='home'),
    path('login/',login_user, name ='login'),
    path('viewcart/',viewcart_user, name = 'viewcart'),
    path('addbook/',addbook_user, name = 'addbook'),
    path('register/',register_user, name ='register'),
    path('logout/',logout_user, name = 'logout'),
    path('addtocart/<str:pk>', addtocart_user,name='addtocart'),           
]



