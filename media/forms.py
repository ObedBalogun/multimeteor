from django.forms import ModelForm
from django import forms
from .models import Post,Media

class PostForm(forms.ModelForm):
    content = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Whats Happening?'}), label="")

    class Meta:
        model = Post
        fields = ('content',)

class GalleryForm(ModelForm):
    class Meta:
        model = Media
        fields = ('files',)