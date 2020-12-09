from django.shortcuts import render, HttpResponse, redirect
import random

# store a random number in session??

# Create your views here.
def index(request):
    if "random_num" not in request.session:
        request.session["random_num"] = random.randint(100)
        print(request.session["random_num"])

    # some logic to compare guess to random number
    # 

    print("Inside index route!!")
    return render(request, "index.html")

def process_guess(request):
    print("Inside process guess")
    print(request.POST)
    print(request.POST["guess"])
    # do I need to save anything past this function call?
    # Save guess in session


    return redirect('/')