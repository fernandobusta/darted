from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


def index(request):
    return render(request, 'comertial2/index.html')

def mines(request):
    return render(request, 'comertial2/mines.html')

def about(request):
    return render(request, 'comertial2/about.html')


def joinTeamView(request):
    if request.method == "POST":
        # User has filled in the form
        # and is sending data back
        form = JoinTeamForm(request.POST)
        if form.is_valid():
            join_t = form.save()
            return redirect('index')
        else:
            return render(request, 'comertial2/jointeam.html', {'form':form})
    else:
        form = JoinTeamForm()
        return render(request, 'comertial2/jointeam.html', {'form':form})
    
def completed(request):
    return render(request, 'comertial2/completed.html')


# Contact View and form
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cont = form.save()
            return redirect('index')
        else:
            return render(request,'comertial2/contact.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'comertial2/contact.html', {'form': form})

def test(request):
    return render(request, 'comertial2/test.html')