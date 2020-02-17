from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index),
    path('areas/<area>', views.areas),
    path('areas/<area>/results', views.results),
    path('polls/<int:poll_id>', views.polls),
    path('candidates/<name>/', views.candidates),
]
