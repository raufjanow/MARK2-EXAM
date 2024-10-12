from django.db import models

class header_top(models.Model):
    number = models.IntegerField()
    text = models.CharField(max_length=255)
    joined_on = models.DateField()

class header_middle(models.Model):
    title = models.CharField(max_length=255)

class header_bot(models.Model):
    text2 = models.CharField(max_length=255)
    description = models.TextField()
