from django.shortcuts import render, redirect
from .models import Show

# Create your views here.

def dashboard(request):

    return render(request, "dashboard.html")

def new_page(request):
    return render(request, "new.html")

def edit_page(request, show_id):
    print("edit show id: ", show_id)
    return render(request, "edit.html")

def show_page(request, show_id):
    print("show page id: ", show_id)
    return render(request, "show.html")

# Action and Post routes (will redirect)
def delete(request, show_id):
    print("delete show id: ", show_id)
    # delete something in the db!
    return redirect('/shows')

def create_show(request):
    print("Create show function")
    print(request.POST)

    # test if request.post is all good
    errors = Show.objects.validateShow(request.POST)

    print(errors)
    
    if errors:
        print("Try again.")
        return redirect('/shows/new')
    
    new_show = Show.objects.create(
        title=request.POST["title"],
        description=request.POST["description"],
        network=request.POST["network"],
        release_date=request.POST["release_date"],
        )
    print(Show.objects.all())

    return redirect('/shows/' + str(new_show.id))

