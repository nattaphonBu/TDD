from django.contrib import admin
from .models import Sentiment

class AdminSentimentModelList(admin.ModelAdmin):
    list_view = ['word', 'sentiment']
    list_filter = ['word']

list_filter = ['word']# Register your models here.
