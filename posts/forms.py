from django import forms
from django.forms import fields
from .models import Post, Comment

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content',]

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content',]

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]
        