from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def Todoloyiha(request):
    if request.method=="POST":
        Todo.objects.create(
            sarlavha=request.POST.get('s'),
            vaqt=request.POST.get('v'),
            izoh=request.POST.get('i'),
            maqsad=request.POST.get('m')
        )
        return redirect('/todo/')
    data={
        "todo":Todo.objects.all()
    }
    return render(request,"todo.html",data)
def todoochir(request,pk):
    data={
        "todo":Todo.objects.get(id=pk).delete()
    }
    return redirect("/todo/")
