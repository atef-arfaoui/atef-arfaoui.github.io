__author__ = 'miner'
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth as authen
from django.core.context_processors import csrf
from forms import UserCreationForm
from .forms import InputForm

import subprocess


def login(request):
    c={}
    c.update(csrf(request))
    return render(request, 'registration/login.html', c)

def index(request):
    return  render(request, 'base.html')
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authen.authenticate(username=username, password=password)

    if user is not None:
        authen.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

data_user=""
def loggedin(request):
    global data_user
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            #data_user = form.cleaned_data['input_user']
            #twitter_stream.filter(track=[data_user])
            #time.sleep(6)
            #p = subprocess.Popen(['/usr/bin/python2', '/home/miner/Desktop/analyse-it/twitter_mining/rename_tweets.py',data_user ], close_fds=True)
            #p2 = subprocess.Popen(['/usr/bin/python2', '/home/miner/Desktop/analyse-it/twitter_mining/generate_graph.py' ], close_fds=True)
            #p2.terminate()
            #p.terminate()
            return HttpResponseRedirect('#')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InputForm()
    return render(request, 'registration/loggedin.html',
                  {'full_name': request.user.username, 'form': form})


print data_user
def invalid_login(request):
    return render(request, 'registration/invalid_login.html')


def logout(request):
    authen.logout(request)
    return  render(request, 'registration/logout.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()

    return render(request, 'registration/register.html', args)

def register_success(request):
    return render(request, 'registration/register_success.html')