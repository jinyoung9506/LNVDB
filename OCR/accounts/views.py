from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User, UserManager
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def account(request):
    if not request.user.is_authenticated:
        return render(request, 'accounts/login.html')
    else:
        user = request.user
        return render(request, 'account/def.html',{'user':user})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            messages.info(request,'로그인 성공!')
            return render(request, 'accdef', )
        else:
            return render(request, 'accounts/login.html', {'error':'Login Failed'})        
    else:
        return render(request, 'accounts/login.html')

#def signup(request):
#   return render(request, 'accounts/signup.html')

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username = request.POST['username'],
                password = request.POST['password1'],
                email= request.POST['email']
            )
            auth.login(request,user)
            return render(request, {'Sign up Success'})
        else:    
            return render(request, 'accounts/signup.html', {'error':'Sign up Failed'})
    else:
        return render(request, 'accounts/signup.html')

@login_required
def logout(request):
    auth.logout(request)
    return render(request, 'accdef')