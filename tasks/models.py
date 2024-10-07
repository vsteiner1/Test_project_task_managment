# tasks/models.py
from django.db import models

class Task(models.Model):
    CATEGORY_CHOICES = [
        ('work', 'Work'),
        ('personal', 'Personal'),
        ('shopping', 'Shopping'),
        ('other', 'Other'),
    ]
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    completed = models.BooleanField(default=False)  

    def __str__(self):
        return self.title
