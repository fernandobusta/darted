from django.db import models


class ContactEmail(models.Model):
    """Emails entered in the Launch page"""
    id = models.AutoField(primary_key=True)
    email = models.EmailField()

    def __str__(self):
        """String representation of email"""
        return self.email
    

class JoinTeam(models.Model):
    """People interested in joinning the team"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    other = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} -> with email: {self.email}, from: {self.city}, says: {self.other}'