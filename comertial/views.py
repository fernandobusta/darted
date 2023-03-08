from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *



def questionsView(request):
    if request.method == "POST":
        # User has filled in the form
        # and is sending data back
        form = QuestionForm(request.POST)
        if form.is_valid():
            quest = form.save()
            return redirect('index')
        else:
            return render(request, 'comertial2/questions.html', {'form':form})
    else:
        form = QuestionForm()
        return render(request, 'comertial2/questions.html', {'form':form})
    
def completed(request):
    return render(request, 'comertial2/completed.html')



# This is for the new template ==========================================================
def index(request):
    return render(request, 'comertial2/index.html')

def mines(request):
    return render(request, 'comertial2/mines.html')

def about(request):
    return render(request, 'comertial2/about.html')

def contact(request):
    return render(request, 'comertial2/contact.html')

def test(request):
    return render(request, 'comertial2/test.html')