from django.shortcuts import render
from django.views.generic import *

from .forms import *
from .models import *


# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class AboutView(TemplateView):
    template_name = "about.html"

 
class BlogListView(ListView):
    template_name = "bloglist.html"
    queryset = Blog.objects.all()
    context_object_name = "allblogs"


class BlogDetailView(DetailView):
    template_name = "blogdetail.html"
    model = Blog
    context_object_name = "blogobject"


class BlogCreateView(CreateView):
    template_name = "blogcreate.html"
    form_class = BlogForm
    success_url = "/blogs/"


class BlogUpdateView(UpdateView):
    template_name = "blogcreate.html"
    form_class = BlogForm
    model = Blog
    success_url = "/blogs/"


class BlogDeleteView(DeleteView):
    template_name = "blogdelete.html"
    # form_class = BlogForm
    model = Blog
    success_url = "/blogs/"
