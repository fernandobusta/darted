from django.urls import path, include 
from .views import *

urlpatterns = [
   
   # Form
   path('jointeam', joinTeamView, name='jointeam'),

   # For the new template
   path('', index, name="index"),
   path('mines', mines, name="mines"),
   path('about', about, name="about"),
   path('test', test, name="test"),
   path('contact', contact, name="contact"),

]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]