from django import forms
from .models import Post, Comments

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        exclude = ['slug']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }




