from django.shortcuts import render
from django.views.generic import ListView, DetailView
# from django.views.generic.edit import 
from .models import Blog_page

# Create your views here.
class BlogHomePage(ListView):
    model = Blog_page
    template_name = 'index.html'
    context_object_name = 'object_list'

class UpdateHomePage(DetailView):
    model = Blog_page
    template_name = 'update.html'