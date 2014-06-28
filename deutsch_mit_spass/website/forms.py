from django.contrib.auth.models import User
from django import forms
from website.models import Lesson


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class CorrectingExerciseForm(forms.Form):
    correct_sentence = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '1'}))
    second_correct_sentence = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': '1'}),
        required=False)
    wrong_sentence = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '1'}))


class TranslatingExerciseForm(forms.Form):
    example = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '1'}))
    translated_example = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '1'}))


class ReadingExerciseForm(forms.Form):
    CHOICES = ((0, 'False'), (1, 'True'))
    text = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '3'}))
    question = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    first_choise = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    first_is_correct = forms.ChoiceField(choices=CHOICES)
    second_choise = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    second_is_correct = forms.ChoiceField(choices=CHOICES)
    third_choise = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=False)
    third_is_correct = forms.ChoiceField(choices=CHOICES)
    fourt_choise = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=False)
    fourt_is_correct = forms.ChoiceField(choices=CHOICES)


class FillInExerciseForm(forms.Form):
    example = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '1'}))
    correct_answer = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    wrong_answer = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    second_wrong_answer = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))


class OrderingExerciseForm(forms.Form):
    description = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    first = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    second = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    third = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    fourt = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    first_match = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    second_match = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    third_match = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    fourt_match = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))


class LessonForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    difficulty = forms.ChoiceField(choices=Lesson.DIFFICULTIES_CHOISES)
