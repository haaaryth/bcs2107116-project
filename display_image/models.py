from django.db import models

# Create your models here.
class student(models.Model):
    id = models.CharField(max_length = 6, primary_key=True)
    name = models.TextField()
    password=models.TextField(default='NULL')
    