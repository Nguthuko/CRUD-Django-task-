from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import post
from django.http import HttpResponse

# Create your views here.
class BlogListView(ListView):
    model = post
    template_name = 'home.html'
    #return HttpResponse(template_name)

class BlogDetailView(DetailView):
    model = post
    template_name = 'post_detail.html'