from django.db import models
from django.contrib.auth.models import User


class Lesson(models.Model):
    DIFFICULTIES_CHOISES = (
        ("0", "low"),
        ("1", "easy"),
        ("2", "medium"),
        ("3", "hard")
        )
    difficulty = models.CharField(
        max_length=1,
        choices=DIFFICULTIES_CHOISES,
        default="0")

    content = models.TextField()


class TranslationExercise(models.Model):
    example = models.CharField(max_length=300)
    translated_example = models.CharField(max_length=300)


class FillInExercise(models.Model):
    example = models.CharField(max_length=300)
    correct_answer = models.CharField(max_length=20)
    wrong_answer = models.CharField(max_length=20)
    second_wrong_answer = models.CharField(max_length=20)


class ReadingExercise(models.Model):
    text = models.TextField()
    question = models.CharField(max_length=300)


class Choice(models.Model):
    text = models.CharField(max_length=50)
    exercise = models.ForeignKey(ReadingExercise)
    is_correct = models.SmallIntegerField(choices=(
        (0, 'False'), (1, 'True')), default=0)


class CorrectingExercise(models.Model):
    correct_sentence = models.CharField(max_length=300)
    second_correct_sentence = models.CharField(max_length=300, default="")
    wrong_sentence = models.CharField(max_length=300)


class OrderingExercise(models.Model):
    description = models.CharField(max_length=50)
    first = models.CharField(max_length=20)
    second = models.CharField(max_length=20)
    third = models.CharField(max_length=20)
    fourt = models.CharField(max_length=20)
    first_match = models.CharField(max_length=20)
    second_match = models.CharField(max_length=20)
    third_match = models.CharField(max_length=20)
    fourt_match = models.CharField(max_length=20)


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    STUDENT = 0
    TEACHER = 1
    ROLE_CHOISES = (
        (STUDENT, "Student"),
        (TEACHER, "Teacher")
        )
    role = models.SmallIntegerField(
        choices=ROLE_CHOISES,
        default=0
        )
