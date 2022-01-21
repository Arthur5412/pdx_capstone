# from math import fabs
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import login,logout,authenticate
from .forms import *
from django.contrib.auth.decorators import login_required




from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    books = Book.objects.all()
    if request.user.is_staff:
        return render(request,'bookstore/home.html',{
            'books':books
        })
    else :
         return render(request,'bookstore/home.html',{
            'books': books
        })


#this function checks of the use is authenticated or not
def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method =="POST":
            username =request.POST.get('username')
            password =request.POST.get('password')
            user=authenticate(request, username = username,password =password)
            if user is not None:
                print("Working on it")
                login(request,user)
                return redirect('home')
            
        return render(request,'bookstore/login.html',{

            })
            
#we define a function for the logout
def logout_user(request):
    logout(request)
    return redirect('home')

#we define a function for the registration page
def register_user(request):
    form = NewUserForm()
    member_form =NewMemberForm()
    if request.method =="POST":
        form=NewUserForm(request.POST)
        member_form=NewMemberForm(request.POST)
        if form.is_valid() and member_form.is_valid():
            user=form.save()
            member = member_form.save(commit=False)
            member.user=user
            member.save()
            return redirect('login')
    return render(request,'bookstore/register.html',{
        'form':form,
        'member_form':member_form,
    })

# @login_required
def addbook_user(request):
    form =NewBookForm()
    if request.method =="POST":
        form =NewBookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    
    return render(request,'bookstore/addbook.html',{
        'form':form
    })

# @login_required
def viewcart_user(request):
    memb = Member.objects.filter(user=request.user)
    for me in memb:
        carts = Cart.objects.all()
        for cart in carts:
            if(cart.memeber == me):
                return render(request,'bookstore/viewcart.html',{
                    'cart':cart
                })
            else :
                return render(request,'bookstore/empty.html')
# @login_required
def addtocart_user(request,pk):
    book =Book.objects.get(id=pk)
    memb=Member.objects.filter(user=request.user)

    for me in memb:
        carts =Cart.objects.all()
        reqcart =''
        for cart in carts:
            if(cart.member == me):
                reqcart=cart
                break
        if(reqcart==''):
            reqcart=Cart.objects.create(
                member = me,
                )
        reqcart.books.add(book)
    return redirect('home')


