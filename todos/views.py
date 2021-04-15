from django.shortcuts import render
from . models import MyModel

# Create your views here.


def index(request):
    todos = MyModel.objects.all()
    return render(request, "index.html", {"data": todos})
