from asosiy.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', Todoloyiha),
    path('delete/<int:pk>', todoochir),
]
