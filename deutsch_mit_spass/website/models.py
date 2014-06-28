from django.db import models
from django.contrib.auth.models import User


class Lesson(models.Model):
    """Lesson created by teachers

    Attributes:
    content -- Content of the lesson(text)
    difficulty -- difficulty of the lesson
    """
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
    '''Translation exercise created by teacher'''
    example = models.CharField(max_length=300)
    translated_example = models.CharField(max_length=300)


class FillInExercise(models.Model):
    '''Gap fill exercise

    Example with a gap and 3 options to fill in
    '''
    example = models.CharField(max_length=300)
    correct_answer = models.CharField(max_length=20)
    wrong_answer = models.CharField(max_length=20)
    second_wrong_answer = models.CharField(max_length=20)


class ReadingExercise(models.Model):
    '''Reading exercise has text and question'''
    text = models.TextField()
    question = models.CharField(max_length=300)


class Choice(models.Model):
    '''Choices wich are reated to question from reading exercise

    It has a contains field to check it the chosen answer is correct
    Attributes:
    text -- text of the choice
    exercise -- reading exercise to map with it's question
    is_correct -- is it correct
    '''
    text = models.CharField(max_length=50)
    exercise = models.ForeignKey(ReadingExercise)
    is_correct = models.SmallIntegerField(choices=(
        (0, 'False'), (1, 'True')), default=0)


class CorrectingExercise(models.Model):
    '''Correcting exercise created by teacher'''
    correct_sentence = models.CharField(max_length=300)
    second_correct_sentence = models.CharField(max_length=300, default="")
    wrong_sentence = models.CharField(max_length=300)


class OrderingExercise(models.Model):
    '''Ordering exercise created by teacher'''
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
    '''User profile

    It shows the role of the user if it is a teacher or student
    linked to User
    Attributes:
    user -- mapping to User
    role -- Student or Teacher
    '''
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
