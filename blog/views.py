from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView

# Create your views here.
@login_required
def home_view(request):

    context = {
        'posts' : Post.objects.all()
    }

    return render(request, 'blog/Home.html', context)

class postListView(ListView):
    model = Post
    template_name = 'blog/Home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class postCreateView(CreateView):
    model = Post
    fields = ['content', 'author']


def profile_view(request):
    return render(request, 'blog/profile.html')