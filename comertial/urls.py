from django.urls import path, include 
from .views import *

urlpatterns = [
   path('index', index, name="index"),
   path('contact', contact, name="contact"),
   path('riddle', riddle, name="riddle"),
   path('mineswp', mineswp, name="mineswp"),
   path('', homepage, name="homepage"),
   path('simple', simple, name="simple"),
   path('completed', completed, name="completed"),
   
   # Form
   path('questions', questionsView, name='questions')

]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]