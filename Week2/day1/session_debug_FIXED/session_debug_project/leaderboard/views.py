from django.shortcuts import render, redirect

# Create your views here.
def index(request): 
    print("In index route")
    # request.session.clear()
    # print(request.session)
    print("render call: ", render(request, "index.html"))
    return render(request, "index.html")


def leaderBoard(request):

    print(request.session)

    if "user_name" not in request.session:
        print('redirecting...')
        return redirect('/')

    ranks = ["first", "second", "third"]
    
    for key in ranks:
        if key not in request.session:
            request.session[key] = 'Please assign a rank.'


    return render(request, "leaderboard.html", {'first': request.session['first'], 'second': request.session['second'], 'third': request.session['third']})

def show(request, rank):

    print(request.session['first'])
    print("Rank passed through the url: ", rank)

    name = ""

    print("Rank is passed in as a ", type(rank))

    if rank == 1:
        if request.session['first'] == "Please assign a rank.":
            return redirect('/leaderboard')
        name = request.session['first']
        print(name)
    elif rank == 2:
        if request.session['second'] == "Please assign a rank.":
            return redirect('/leaderboard')
        name = request.session['second']
    else:
        if request.session['third'] == "Please assign a rank.":
            return redirect('/leaderboard')
        name = request.session['third']

    return render(request, "showFriend.html", {'rank':rank, 'name': name })

def enter(request):
    print(request.POST)
    name = request.POST["FirstName"] + " " + request.POST["Last_Name"]
    request.session['user_name'] = name
    return redirect('/leaderboard')

def changeRanks(request):

    print(request.POST)

    if len(request.POST['first']) > 0:
        request.session['first'] = request.POST['first']
    if len(request.POST['second']) > 0:
        request.session['second'] = request.POST['second']
    if len(request.POST['third']) > 0:
        request.session['third'] = request.POST['third']

    return redirect('/leaderboard')

def logout(request):
    request.session.clear()
    return redirect('/')
