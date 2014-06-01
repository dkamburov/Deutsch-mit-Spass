from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

class Lesson(models.Model):
    DIFFICULTIES_CHOISES = (
            ("0", "low"),
            ("1", "easy"),
            ("2", "medium"),
            ("3", "hard")
        )
    difficulty = models.CharField(max_length=1,
       choices=DIFFICULTIES_CHOISES,
       default="0")

    content = models.TextField()


class TranslationExercise(models.Model):
    example = models.CharField(max_length=300)
    translated_example = models.CharField(max_length=300)


#class FillInExercise(models.Model):
#    pass


class ReadingExercise(models.Model):
    text = models.TextField()
    question = models.CharField(max_length=300)


class Choice(models.Model):
    text = models.CharField(max_length=50)
    excercise = models.ForeignKey(ReadingExercise)

class CorrectingExercise(models.Model):
    correct_sentence = models.CharField(max_length=300)
    wrong_sentence = models.CharField(max_length=300)

#class OrderingExercise(models.Model):
#    pass


class User(AbstractUser):
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

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
