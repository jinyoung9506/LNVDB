from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('areas/<area>', views.areas),
    path('polls/<int:poll_id>/', views.polls)
]
