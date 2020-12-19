from django.shortcuts import render
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    # renders log in and reg page
    return render(request, "index.html")


def register(request):

    # Validate the user input from the form using 
    # User.objects.name_of_your_validate_method(request.POST)
    #  -- comparing the password with the pw confirm
    # Logic to check if email already in database
    input_password = request.POST["password"]

    pw_hash = bcrypt.hashpw(input_password.encode(), bcrypt.gensalt()).decode()
    print(pw_hash)

    user = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'], 
        password=pw_hash
        )
    request.session['user_id'] = user.id

    return redirect('/success')

def log_in(request):
    # objects.get will fail/error out if not in the database
    # get the user from the database -- if list is empty
    # you know there is no user with that email
    userListExists = User.objects.filter(email=request.POST['email'])
    #  [<User object (3)>] (for example)  or  [] if not in db
    if userListExists:
        user = userListExists[0]
        #                password input from form           hashed pw from database
        if bcrypt.checkpw(request.POST['password'].encode(), user.pw_hash.encode()):
            # if we get True after checking the password, we may put the user id in session
            request.session['user_id'] = user.id
            # never render on a post, always redirect!
            return redirect('/success')
    

def logout(request):
    request.session.clear()
    return redirect('/')

def dashboard(request):
    if "user_id" not in request.session():
        messages.error("Please log in.")
        return redirect('/')
    return render(request, "dashboard.html")
