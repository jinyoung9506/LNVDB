from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.account, name = 'accdef'),
    path('login/', views.login, name = 'lin'),
    path('signup/', views.signup, name = 'sup' ),
    path('logout/', views.logout, name = 'lout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
