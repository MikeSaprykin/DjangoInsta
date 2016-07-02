from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic

from content.forms import PhotoPostForm
from content.models import PhotoPost


def home_view(request):
    return render(request, 'templates/home.html')


class UserView(generic.DetailView, generic.CreateView, generic.FormView):
    form_class = PhotoPostForm
    queryset = User.objects.all()
    model = User
    template_name = "user.html"

    def post(self, request, *args, **kwargs):

        return super(UserView, self).post(request, *args, **kwargs)










