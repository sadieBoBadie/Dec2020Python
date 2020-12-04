from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    print("Hello from index")
    return render(request, "index.html")

def process_form(request):

    print(f"CHARGING CREDIT CARD for {request.POST['amount']}!!")
    # print(f"POST: {request.POST}")
    # print(f"GET: {request.GET}")
    return redirect("/success")

def success(request):
    return render(request, "success.html")