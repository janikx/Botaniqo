from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "home.html", {"todos": items})
