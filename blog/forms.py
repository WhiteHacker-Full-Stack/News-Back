from django import forms
from .models import Newslatter,Comment

class NewsForm(forms.ModelForm):
    class Meta:
        model = Newslatter
        fields = ['email']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'emailComment', 'subject', 'message']
