from django.shortcuts import render
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
