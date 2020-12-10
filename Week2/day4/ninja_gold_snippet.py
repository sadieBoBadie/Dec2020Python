# from django.shortcuts import render, HttpResponse

# A possible approach to the process_money function.
# this assumes you have initialized goldCount and 
# messageLog in the root route.

def process_money(request):
    # Make a dictionary, the key is location, value
    location = request.POST['location']
    
    goldFrom = {
        'farm': random.randint(10, 20),
        'cave': random.randint(5, 10),
        'house': random.randint(2, 5),
        'casino': random.randint(-50, 50)
        }

    request.session['goldCount'] += goldFrom[location]
    if goldFrom[location] > 0:
        request.session['messageLog'].append(
            {
                "message":f"You gain {goldFrom[location]} gold!", 
                "class": "green"
            }
        )
    else:
        request.session['messageLog'].append(
            {
                "message":f"You lose {goldFrom[location]} gold!", 
                "class": "red"
            }
        )
    request.session.save()

    return redirect('/')