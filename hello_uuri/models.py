from django.db import models

# Create your models here.

class User(models.Model):
    userId = models.CharField(max_length=100)
    total = models.IntegerField(null=True, blank=True)
    
class Question(models.Model):
    question = models.CharField(max_length=100)
    answer = models.IntegerField()
    userId = models.ForeignKey('User', on_delete=models.CASCADE)
    