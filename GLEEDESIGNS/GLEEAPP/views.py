from django.shortcuts import render, redirect
from .forms import IMAGESForm
from .models import IMAGES

from django.http import HttpResponse
# Create 9i95ti9i95i988888888ws here.
def home(request):
    return render(request, 'GLEEAPP/index.html')

def index2(request):
    return render(request, 'GLEEAPP/index2.html')
def controller(request):
    return render(request, 'GLEEAPP/controller.html')



def IMAGESList(request):
    IMAGE = IMAGES.objects.all()
    return render(request, 'GLEEAPP/list.html', {'IMAGE': IMAGE})


def uploadIMAGES(request):
    if request.method == 'POST':
        form = IMAGESForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index2')
    else:
        form = IMAGESForm()
    return render(request, 'GLEEAPP/upload.html', {'form': form})


def deleteIMAGES(request, pk):
    if request.method == 'POST':
         IMAGE= IMAGES.objects.get(pk=pk)
         IMAGE.delete()
    return redirect('IMAGES_list')



