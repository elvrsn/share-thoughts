from django.db import models

class TextTable(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    tags = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    timestamp = models.CharField(max_length=50)

class Category(models.Model):
    name = models.CharField(max_length=50)

class VisitorFeedback(models.Model):
    ip = models.CharField(max_length=50)
    comments = models.TextField(null=True)
    timestamp = models.CharField(max_length=50)

class MediaTable(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(null=True)
    url =  models.URLField()
    tags = models.CharField(max_length=500)
    timestamp = models.CharField(max_length=50)
