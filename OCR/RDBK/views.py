from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import RequestContext
from .forms import UploadFileForm
from .models import FileModel

# Create your views here.
def index(request):
    form = UploadFileForm()
    return render(request, 'RDBK/index.html',{'form':form})

def files(request):
    return render(request, 'RDBK/file.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            up = FileModel(upload=request.FILES['upfile'])
            up.save()
            return HttpResponseRedirect('/success/')
        else:
            return HttpResponse('업로드실패')
    else:
        form = UploadFileForm()

    return render(request, 'RDBK/index.html',{'form':form})


