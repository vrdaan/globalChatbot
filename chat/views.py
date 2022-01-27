from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout

def index(request):
    return render(request, 'chat/login.html', {})

def user_logout(request):
    logout(request)
    return redirect('/')

def user_auth(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        groupcode = request.POST['groupcode']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user.
            return redirect('chat/%s/' % groupcode)
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'chat/login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, '')

@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
    }) 