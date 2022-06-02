from django import forms
from .models import *

class WriteForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
