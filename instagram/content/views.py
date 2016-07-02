from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic

from content.forms import PhotoPostForm
from content.models import PhotoPost


def home_view(request):
    return render(request, 'home.html')


class UserView(generic.DetailView, generic.FormView):
    form_class = PhotoPostForm
    queryset = User.objects.all()
    model = User
    template_name = "user.html"


class CreatePostView(generic.CreateView):
    form_class = PhotoPostForm
    template_name = "succes_upload.html"








