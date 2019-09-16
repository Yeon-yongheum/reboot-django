from django.db import models

# Create your models here.
# Reporter(1) - Article(N)
# reporter - name
class Reporter(models.Model):
    name = models.CharField(max_length=10)

class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

# Article(1) - Comment(N)
# Comment - content
class Comment(models.Model):
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add = True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    