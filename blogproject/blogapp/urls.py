from django.urls import path
from .views import *

app_name = "BlogApp"
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('about/', AboutView.as_view(), name="about"),
    path('blogs/', BlogListView.as_view(), name="bloglist"),
    path('blogs/<int:pk>/detail/', BlogDetailView.as_view(), name="blogdetail"),
    path('blogs/create/', BlogCreateView.as_view(), name="blogcreate"),
    path('blogs/<int:pk>/update/', BlogUpdateView.as_view(), name="blogupdate"),
    path('blogs/<int:pk>/delete/', BlogDeleteView.as_view(), name="blogdelete"),
]
