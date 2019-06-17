from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class CheckWords(TemplateView):
    template_name = 'index.html'
    def get(self, request):
        return render(request,self.template_name,{})


