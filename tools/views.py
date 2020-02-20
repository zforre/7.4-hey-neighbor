from django.shortcuts import render
from django.views import generic
from .models import Tool

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'tools/index.html'
    model = Tool