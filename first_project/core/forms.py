from django import forms
from .models import Post 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'category', 'body']

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'category', 'body']
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'px-5 py-3 rounded-lg ring-1'}),
        #     'category': forms.Select(attrs={'class': 'form-control'}),
        #     'body': forms.Textarea(attrs={'class': 'form-control'}),
        # }