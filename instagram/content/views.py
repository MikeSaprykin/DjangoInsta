from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic

from content.forms import PhotoPostForm
from content.models import PhotoPost


def home_view(request):
    return render(request, 'home.html')


class UserView(generic.DetailView):
    model = User
    template_name = "user.html"


class PostView(generic.DetailView):
    model = User
    template_name = "post.html"


class CreatePostView(generic.CreateView):
    # form_class = PhotoPostForm
    model = PhotoPost
    template_name = "upload.html"
    fields = ['author', 'image', 'description']











