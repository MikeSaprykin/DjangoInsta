from django import forms
from .models import *


class PhotoPostForm(forms.Form):
    class Meta:
        model = PhotoPost


class CommentForm(forms.Form):
    class Meta:
        model = Comment
