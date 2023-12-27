from django.shortcuts import render,redirect
from app.models import *
from django.http import HttpResponseRedirect,HttpResponse

from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password=request.POST.get('password')
        image = request.FILES.get('image')
        regestration=Regestration.objects.create(name=name,image=image,password=password)
        messages.success(request, 'Registration successful!')
        return HttpResponseRedirect(request.path_info)

    return render(request,"base.html")