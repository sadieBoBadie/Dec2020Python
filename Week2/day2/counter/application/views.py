from django.shortcuts import render, HttpResponse, redirect

# request.session = {}
# Create your views here.
def index(request):

    if 'count' in request.session:
        request.session["count"] += 1
    else:
        request.session["count"] = 1

    return render(request, "index.html")

def destroy(request):
    request.session.clear()
    return redirect('/')
