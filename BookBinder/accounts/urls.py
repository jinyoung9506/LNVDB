from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.account, name = 'accdef'),
    path('', views.account, name = 'home'),
    path('login/', views.loginform, name = 'linform'),
    path('dologin/', views.login, name = 'lin'),
    path('signup/', views.signupform, name = 'supform' ),
    path('dosignup/', views.signup, name = 'sup' ),
    path('logout/', views.logout, name = 'lout'),
    path('readdata/', views.readdata, name = 'readdata'),
    path(r'delete/(?P<isbn>\d{13})/', views.delete, name = 'delete'),
    path('loginfromand/', views.loginfromand, name = 'linfand'),
    path('logoutfromand/', views.logoutfromand, name = 'loutfand'),
    path('upfromjson/', views.upfromjson, name = 'linfjson'),
    path('downtojson/', views.downtojson, name = 'dwntjson'),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
