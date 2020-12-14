from django.shortcuts import render, redirect
from .models import Task

def index(request):
    print("In index route")

    context = {
        "all_tasks": Task.objects.all()
    }

    return render(request, "index.html", context)

# post request! from form
def create_task(request):
    print(request.POST)
    print('*'*30)

    validate(request.POST)


    Task.objects.create(
        title=request.POST["title"],
        description=request.POST["description"],
        due_date = request.POST["due_date"]
        )
    print(Task.objects.all())
    return redirect('/')

def validate():
    return errors