from django.contrib.auth.models import User
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
    second_correct_sentence = forms.CharField(
        widget=forms.Textarea,
        required=False)
    wrong_sentence = forms.CharField(widget=forms.Textarea)


class TranslatingExerciseForm(forms.Form):
    example = forms.CharField(widget=forms.Textarea)
    translated_example = forms.CharField(widget=forms.Textarea)


class ReadingExerciseForm(forms.Form):
    CHOICES = ((0, 'False'), (1, 'True'))
    text = forms.CharField(widget=forms.Textarea)
    question = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'special'}))
    first_choise = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'special'}))
    first_is_correct = forms.ChoiceField(choices=CHOICES)
    second_choise = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'special'}))
    second_is_correct = forms.ChoiceField(choices=CHOICES)
    third_choise = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'special'}), required=False)
    third_is_correct = forms.ChoiceField(choices=CHOICES)
    fourt_choise = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'special'}), required=False)
    fourt_is_correct = forms.ChoiceField(choices=CHOICES)
