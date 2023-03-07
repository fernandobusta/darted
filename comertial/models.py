from django.db import models

class Client(models.Model):
    """Model representing a Client"""
    name = models.CharField(max_length=200, help_text='Enter a name for the client')
    email = models.EmailField()
    

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Player(models.Model):
    """Model representing the Player"""
    email = models.EmailField()
    name = models.CharField(max_length=100)
    result = models.CharField(max_length=200)
    questions = models.TextField()

    def __str__(self):
        """String representing the Player object"""
        return f'{self.name} has the result: {self.result}'


class Question(models.Model):
    """Model for questions on comertial web"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()