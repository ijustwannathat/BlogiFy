from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class SignUpForm(UserCreationForm):
    class_update = {'class': 'form-control mb-1'}
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={**class_update,
                                                'placeholder': 'Enter First Name'}))
    last_name  = forms.CharField(max_length=100, widget=forms.TextInput(attrs={**class_update,
                                                'placeholder': 'Enter Last Name'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={**class_update,
                                                'placeholder': 'Enter Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={**class_update,
                                                'placeholder': 'Enter Email'}))
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={**class_update,
                                                'placeholder': 'Enter Password'}))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={**class_update,
                                                'placeholder': 'Confirm Password'}))



    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']



class LoginForm(AuthenticationForm):
    username = forms.CharField(
                        max_length=100,
                        required=True,
                        widget=forms.TextInput(attrs={
                            'class': 'form-control mb-1',
                            'placeholder': 'Username'})
    )

    password = forms.CharField(
                        max_length=100,
                        required=True,
                        widget=forms.PasswordInput(attrs={
                            'class': 'form-control mb-1',
                            'placeholder': 'Password'})
    )

    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']



class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(
                        max_length=100,
                        required=True,
                        widget=forms.TextInput(attrs={
                            'class': 'form-control mb-1',
                            'placeholder': 'Username'})
    )
    email = forms.EmailField(
                        required=True,
                        widget=forms.TextInput(attrs={
                            'class': 'form-control mb-1',
                            'placeholder': 'Email'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']



class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={
                            'class': 'form-control mb-1'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
