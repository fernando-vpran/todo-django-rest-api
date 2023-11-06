from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    done = models.BooleanField(default=False)