from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

def todo_list(request):
    if request.method == "POST":
        title = request.POST.get("title")
        Todo.objects.create(title=title)

        return redirect("/todo/")

    todos = Todo.objects.all()
    return render(request, "todo/list.html", {"todos": todos})
# Create your views here.


