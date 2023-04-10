from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def Todoloyiha(request):
    data={
        "todo":Todo.objects.all()
    }
    return render(request,"todo.html",data)

