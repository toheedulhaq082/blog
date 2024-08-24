from django.shortcuts import render
from django.views.generic import ListView
from blog.models import BlogModel

# Create your views here.
class HomePageView(ListView): 
    template_name = 'home.html'
    model = BlogModel
    context_object_name = 'all_posts_list'

    def get_queryset(self):
        return BlogModel.objects.all().order_by('-created_at')[:5]