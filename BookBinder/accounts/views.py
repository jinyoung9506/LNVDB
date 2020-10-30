from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, JsonResponse
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User, UserManager
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import Book
import requests
import json
# Create your views here.

def account(request):
    if not request.user.is_authenticated:
        storage = messages.get_messages(request)
        storage.used = True
        return redirect('accounts:linform')
    else:
        user = User.objects.get(username = request.user.username)
        book = Book.objects.all()
        book = Book.objects.filter(owner = user.username)
        count = book.count()
        storage = messages.get_messages(request)
        storage.used = True
        return render(request, 'accounts/def.html', {'user':user, 'books':book, 'count':count})

def deletedata(request, isbn):
    if not request.user.is_authenticated:
        storage = messages.get_messages(request)
        storage.used = True
        return redirect('accounts:linform')
    else:
        user = User.objects.get(username = request.user.username)
        book = Book.objects.all()
        book = book.filter(owner = user.username).filter(isbn = isbn)
        book.delete()
        book = Book.objects.filter(owner = user.username)
        count = book.count()
        storage = messages.get_messages(request)
        storage.used = True
        return render(request, 'accounts/def.html', {'user':user, 'books':book, 'count':count})

#def readdatafromand(request):

#def senddatatoand(request):

def downtojson(request):
    if request.method=="POST":   
        data = json.loads(request.body)
        username = data['username']
        password = data['password']

        user = auth.authenticate(request, username = username, password = password)
        
        if user is not None:
            try:
                auth.login(request,user)
                book = Book.objects.all().filter( owner = username)
                booklist = serializers.serialize('json', book)
                return HttpResponse(booklist, content_type = "text/json-comment-filtered")
            except:
                return JsonResponse({"result", "LoginFail"}) 
        else:
            return JsonResponse({"result", "LoginFail"}) 
    else:
        return JsonResponse({"result", "LoginFail"}) 


def upfromjson(request):
    data = json.loads(request.body)

    if request.user.is_authenticated:
        return HttpResponse("AlreadyLoginned")
    if request.method == "POST":
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        isbn = data['isbn']
        title = data['title']
        booklink = data['booklink']
        author = data['author']
        price = data['price']
        publisher = data['publisher']
        date = data['date']
        imagelink = data['imagelink']
        memo = data['memo']

        user = auth.authenticate(request, username = username, password = password)
        
        if user is not None:
            try:
                auth.login(request,user)
                Book.create( owner = username, isbn = isbn, title = title, booklink = booklink, author = author, price = price, publisher = publisher, date = date, imagelink = imagelink, memo = memo )
                return JsonResponse({"title" : title, "result": "success"})
            except:
                book = Book.objects.all()
                book = book.filter( owner = username, isbn = isbn)
                book.delete()
                Book.objects.create( owner = username, isbn = isbn, title = title, booklink = booklink, author = author, price = price, publisher = publisher, date = date, imagelink = imagelink, memo = memo )
                return JsonResponse({"title" : title, "result": "success"})
            else:
                return JsonResponse({"result", "LoginFail"}) 
        else:
            return JsonResponse({"result", "LoginFail"})   
    else:
        return JsonResponse({"result", "LoginFail"})

def loginfromand(request):
    if request.user.is_authenticated:
        return HttpResponse("LoginSuccess")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            try:
                auth.login(request,user)
                return HttpResponse("LoginSuccess")
            except:
                return HttpResponse("LoginFailed")
        else:
            return HttpResponse("LoginFailed")        
    else:
        return HttpResponse("LoginFailed")

@login_required
def logoutfromand(request):
    auth.logout(request)
    return HttpResponse("LogOut")


def login(request):
    if request.user.is_authenticated:
        storage = messages.get_messages(request)
        storage.used = True
        return redirect('accounts:accdef')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            storage = messages.get_messages(request)
            storage.used = True
            messages.success(request,'로그인 성공!')
            return redirect('accounts:accdef')
        else:
            storage = messages.get_messages(request)
            storage.used = True
            messages.error(request,'로그인 실패!')
            return redirect('accounts:linform')        
    else:
        storage = messages.get_messages(request)
        storage.used = True
        messages.error(request, '잘못된 접근입니다')
        return redirect('accounts:accdef')

def signup(request):
    if request.user.is_authenticated:
        storage = messages.get_messages(request)
        storage.used = True
        return redirect('accounts:accdef')

    if (request.POST["username"] is not None) and (request.method == "POST") and (request.POST["password1"] == request.POST["password2"]):
            try:
                user = User.objects.create_user(
                    username = request.POST["username"],
                    password = request.POST["password1"],
                    email= request.POST["email"]
                )
                auth.login(request,user)
                storage = messages.get_messages(request)
                storage.used = True
                messages.success(request,'회원가입 성공!')
                return redirect(request, 'accounts:accdef', {'user':user} )
            except:
                storage = messages.get_messages(request)
                storage.used = True
                return redirect('accounts:supform')
            else:
                storage = messages.get_messages(request)
                storage.used = True
                messages.error(request,'회원가입 실패!')  
                return redirect('accounts:supform')
    else:
        storage = messages.get_messages(request)
        storage.used = True
        messages.error(request, '잘못된 접근입니다')
        return redirect('accounts:accdef')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('accounts:accdef')

def loginform(request):
    if request.user.is_authenticated:
        storage = messages.get_messages(request)
        storage.used = True
        return redirect('accounts:accdef')
    else:
        return render(request, 'accounts/login.html')

def signupform(request):
    if request.user.is_authenticated:
        storage = messages.get_messages(request)
        storage.used = True
        return redirect('accounts:accdef')
    else:
        return render(request, 'accounts/signup.html')