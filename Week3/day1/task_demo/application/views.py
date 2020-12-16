from django.shortcuts import render, redirect
from .models import Task
from django.contrib import messages

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

    errors = Task.objects.getErrors(request.POST)
    print(errors)


    if errors:
        print("There were errors")
        for category, message in errors.items():
            messages.error(request, message, extra_tags=category)
    else:
        print("no errors")
        Task.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            due_date = request.POST["due_date"]
            )
    print(Task.objects.all())
    return redirect('/')
