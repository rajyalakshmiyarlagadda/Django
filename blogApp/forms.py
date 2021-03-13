from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
            'content': forms.TextInput(attrs={'placeholder': 'Please write your valuable content here'})
        }
