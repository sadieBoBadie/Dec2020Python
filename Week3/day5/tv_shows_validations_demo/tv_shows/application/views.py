from django.shortcuts import render, redirect
from .models import Show

# Create your views here.

def dashboard(request):
    context = {
        "shows": Show.objects.all()
    }
    return render(request, "dashboard.html", context)

def new_page(request):
    return render(request, "new.html")

def edit_page(request, show_id):
    # GET THE SHOW FROM THE DB
    print("edit show id: ", show_id)
    return render(request, "edit.html")

def show_page(request, show_id):
    # GET THE SHOW FROM THE DB
    print("show page id: ", show_id)
    return render(request, "show.html")





# Action and Post routes (will redirect)
def delete(request, show_id):
    print("delete show id: ", show_id)
    # delete something in the db!
    return redirect('/shows')

def create_show(request):
    print("Create show in DB function")
    print(request.POST)

    Show.objects.create(
        title = request.POST['title'],
        description = request.POST['title'],
        network = request.POST['title'],
        release_date = request.POST['title']
    )

    return redirect('/shows/1')

def update(request):
    print("Update show in DB function")
    print(request.POST)
    return redirect('/shows/1')

