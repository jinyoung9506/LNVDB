from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, JsonResponse
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User, UserManager
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import Book, Profile
# Create your views here.

def account(request):
    if not request.user.is_authenticated:
        return render(request, 'accounts/login.html')
    else:
        user = request.user
        profile = Profile(user = user)
        samplebook1 = Book( isbn = '9784894652385', title = '精装追男姐', imagelink = 'https://images-na.ssl-images-amazon.com/images/I/91d4ugWffJL.jpg')
        samplebook2 = Book( isbn = '9788926360200', title = '라이트 X 라이트 12', imagelink = 'https://bookthumb-phinf.pstatic.net/cover/116/467/11646733.jpg')
        samplebook3 = Book( isbn = '9791127857097', title = '곰 곰 곰 베어 11.5', imagelink = 'https://bookthumb-phinf.pstatic.net/cover/167/788/16778844.jpg')
        profile.books.add(samplebook1)
        profile.books.add(samplebook2)
        profile.books.add(samplebook3)
        profile.save()
        return render(request, 'accounts/def.html',{'user':user, 'profile':profile})

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
            profile = Profile.objects.get(user = user)
            storage = messages.get_messages(request)
            storage.used = True
            messages.success(request,'로그인 성공!')
            return render(request, 'accounts/def.html',{'user':user, 'profile':profile})
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
    if request.method == "POST":
        if (request.POST["username"] is not None) and (request.POST["password1"] is not None):
            if request.POST["password1"] == request.POST["password2"]:
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
                    return render(request, 'accounts:accdef', {'user':user} )
                except:
                    storage = messages.get_messages(request)
                    storage.used = True
                    messages.error(request,'회원가입 실패!')    
                    return redirect('accounts:supform')
            else:
                storage = messages.get_messages(request)
                storage.used = True
                messages.error(request,'회원가입 실패!')    
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