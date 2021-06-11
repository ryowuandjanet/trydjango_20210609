from django import forms
from posts.models import *

class PostForm(forms.ModelForm):
  class Meta:
    model=Post
    fields=[
      "title",
      "content",
      "image"
    ]

class LandForm(forms.ModelForm):
  post = forms.ModelChoiceField(Post.objects.all(), widget=forms.HiddenInput())
  class Meta:
    model=Land
    fields ='__all__'

  