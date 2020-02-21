from django.shortcuts import render
from django.views import generic
from .models import Tool
from django.urls import reverse
from django.urls import reverse_lazy

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'tools/index.html'
    model = Tool

    # def get_queryset(self):
    #     if 'selection' in self.kwargs:
    #         return Tool.objects.filter(available=self.kwargs['selection'].upper())
    #     return Tool.objects.all()

class ListView(generic.ListView):
    template_name = 'tools/toollist.html'
    model = Tool

class UserView(generic.ListView):
    template_name = 'tools/userlist.html'
    model = Tool

class TemplateView(generic.TemplateView):
    template_name = 'tools/myitems.html'
    model = Tool

