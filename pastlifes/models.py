from django.db import models

# Create your models here.

class Pastlife(models.Model):
    name = models.CharField(max_length=30)
    job = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)