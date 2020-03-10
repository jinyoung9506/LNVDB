from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

app_name = 'RDBK'
urlpatterns = [
    path('', views.index, name = 'home'),
    path('uploading', views.upload_file),
    path('success/',views.files),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
