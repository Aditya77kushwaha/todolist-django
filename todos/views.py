from django.shortcuts import render, redirect
from . models import MyModel

# Create your views here.


def index(request):
    todos = MyModel.objects.all()
    if request.method == "POST":
        a = request.POST['title']
        new = MyModel(task=a)
        new.save()
        print(a)

    return render(request, "index.html", {"data": todos})


def delete(request, pk):
    a = MyModel.objects.get(id=pk)
    a.delete()
    return redirect('/')
