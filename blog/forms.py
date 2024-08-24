from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    class_update = {"class": "form-control mb-1"}
    name = forms.CharField(max_length=25, required=True,
                           widget=forms.TextInput(attrs={
                               **class_update,
                               "placeholder": "Name"}))
    email = forms.EmailField(required=True,
                           widget=forms.TextInput(attrs={
                               **class_update,
                               "placeholder": "Email"}))
    to = forms.EmailField(required=True,
                           widget=forms.TextInput(attrs={
                               **class_update,
                               "placeholder": "To"}))
    comments = forms.CharField(required=False,
                           widget=forms.Textarea(attrs={
                                **class_update,
                                "placeholder": "Comments"}))


class CommentForm(forms.ModelForm):
    class_update = {'class': 'form-control'}
    name = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={
                               **class_update,
                               'placeholder': 'Name'}))
    email = forms.CharField(required=True,
                            widget=forms.EmailInput(attrs={
                                **class_update,
                                'placeholder': 'email'}))
    body = forms.CharField(required=True,
                           widget=forms.Textarea(attrs={
                               **class_update,
                               'placeholder': 'Text'}))

    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class SearchForm(forms.Form):
    query = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class' : 'form-control mb-1',
            'placeholder': 'Enter the title...'}))






