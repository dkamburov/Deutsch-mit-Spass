from website.models import User
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class CorrectingExerciseForm(forms.Form):
    correct_sentence = forms.CharField(widget=forms.Textarea)
    wrong_sentence = forms.CharField(widget=forms.Textarea)
