from django.shortcuts import render, redirect

# request.session = {}

# Create your views here.
def index(request):
    print("Hello from index")
    return render(request, "index.html")

def process_form(request):

    amount = request.POST["amount"]
    request.session["amount_charged"] = amount
    # print(f"POST: {request.POST}")
    # print(f"GET: {request.GET}")
    return redirect("/success")

def success(request):
    print(request.session["amount_charged"])
    return render(request, "success.html")