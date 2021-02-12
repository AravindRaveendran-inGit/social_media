from django import forms
from .models import Post, Comment


class PostModelForm(forms.ModelForm):
    content = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2}))

    class Meta:
        model = Post
        fields = ('content', 'video', 'image')


class CommentModelForm(forms.ModelForm):
    body = forms.CharField(label='',
                           widget=forms.TextInput(attrs={'placeholder': 'Add a comment...'}))

    class Meta:
        model = Comment
        fields = ('body',)
