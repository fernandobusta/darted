from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def index(request):
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits': num_visits,
    }
    return render(request, 'comertial/index.html', context=context)

def contact(request):
    return render(request, 'comertial/contact.html')

def riddle(request):
    return render(request, 'comertial/riddle.html')

def mineswp(request):
    return render(request, 'comertial/mineswp.html')


# Comertial page -> Info about project
def homepage(request):
    return render(request, 'comertial/homepage.html')

def simple(request):
    """Simple view for testing base.html"""
    return render(request, 'comertial/simple.html')

def questionsView(request):
    if request.method == "POST":
        # User has filled in the form
        # and is sending data back
        form = QuestionForm(request.POST)
        if form.is_valid():
            quest = form.save()
            return redirect('completed')
        else:
            return render(request, 'comertial/questions.html', {'form':form})
    else:
        form = QuestionForm()
        return render(request, 'comertial/questions.html', {'form':form})
    
def completed(request):
    return render(request, 'comertial/completed.html')