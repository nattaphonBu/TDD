from django.urls import path
from .views import CheckWords

urlpatterns = [
    path('',CheckWords.as_view(),name='index')
]
