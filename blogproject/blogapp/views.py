from django.shortcuts import render
from django.views.generic import *

# from .forms import *
from .models import *


# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"