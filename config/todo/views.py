from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from django.shortcuts import redirect

def todo_list(request):
    if request.method == "POST":
        title = request.POST.get("title")
        Todo.objects.create(title=title)

        return redirect("home")

    todos = Todo.objects.all()
    return render(request, "todo/list.html", {"todos": todos})
   

def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect("home")
def toggle_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.completed = not todo.completed
    todo.save()
    return redirect("home")
