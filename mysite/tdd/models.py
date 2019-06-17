from django.db import models

class Sentiment(models.Model):
    word = models.CharField(max_length=30)
    sentiment = models.CharField(max_length=30)

