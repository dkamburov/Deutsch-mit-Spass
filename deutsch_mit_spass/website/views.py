from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from website.forms import LoginForm, RegisterForm,\
    CorrectingExerciseForm, TranslatingExerciseForm,\
    ReadingExerciseForm, FillInExerciseForm, OrderingExerciseForm
from website.models import CorrectingExercise, TranslationExercise,\
    UserProfile, ReadingExercise, Choice, FillInExercise, OrderingExercise
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from random import shuffle
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'home.html', locals())


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('welcome')
                else:
                    return redirect('/notlogin')
            else:
                return redirect('/incorrect')
            return HttpResponseRedirect('/thanks/')
    else:
        form = LoginForm()

    return render(request, 'home.html', {
        'form': form,
    })


def welcome(request):
    if request.user.is_anonymous():
        return render(request, 'welcome.html')
    profile = UserProfile.objects.filter(user=request.user)[0]
    role = profile.ROLE_CHOISES[profile.role][1]
    return render(request, 'welcome.html', {
        'username': request.user.username,
        'role': role
    })


def logout_view(request):
    logout(request)
    return redirect('welcome')


def register_view(request):
    data = request.POST if request.POST else None
    form = RegisterForm(data)
    registered = False

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            user_profile = UserProfile()
            user_profile.user = user
            user_profile.role = UserProfile.STUDENT
            user_profile.save()
            registered = True
    return render(request, 'register.html', locals())


@login_required(login_url='/website/login')
def exercises_view(request):
    profile = UserProfile.objects.filter(user=request.user)[0]
    role = profile.ROLE_CHOISES[profile.role][1]
    return render(request, 'exercises.html', {
        'username': request.user.username,
        'role': role
    })


@login_required(login_url='/website/login')
def correction_view(request):
    return add_exercise(
        request,
        CorrectingExerciseForm,
        ('correct_sentence',
            'second_correct_sentence',
            'wrong_sentence'),
        CorrectingExercise.objects,
        'correction.html'
    )


@login_required(login_url='/website/login')
def translation_view(request):
    return add_exercise(
        request,
        TranslatingExerciseForm,
        ('example',
            'translated_example'),
        TranslationExercise.objects,
        'translation.html'
    )


@login_required(login_url='/website/login')
def reading_view(request):
    return add_exercise(
        request,
        ReadingExerciseForm,
        ('text',
            'question'),
        ReadingExercise.objects,
        'reading.html'
    )


def create_choices_reading(exercise, request):
    for choice in ['first', 'second', 'third', 'fourt']:
        if request.POST[choice + '_choise']:
            Choice.objects.create(
                text=request.POST[choice + '_choise'],
                exercise=exercise,
                is_correct=request.POST[choice + '_is_correct'])


@login_required(login_url='/website/login')
def fill_in_view(request):
    return add_exercise(
        request,
        FillInExerciseForm,
        ('example',
            'correct_answer',
            'wrong_answer',
            'second_wrong_answer'),
        FillInExercise.objects,
        'fillin.html'
    )


@login_required(login_url='/website/login')
def ordering_view(request):
    return add_exercise(
        request,
        OrderingExerciseForm,
        ('description',
            'first',
            'second',
            'third',
            'fourt',
            'first_match',
            'second_match',
            'third_match',
            'fourt_match'),
        OrderingExercise.objects,
        'ordering.html'
    )


def add_exercise(request, exercise_form, params, exercise_objects, template):
    profile = UserProfile.objects.filter(user=request.user)[0]
    role = profile.ROLE_CHOISES[profile.role][1]
    if request.method == 'POST' and\
            role == UserProfile.ROLE_CHOISES[UserProfile.TEACHER][1]:
        data = request.POST if request.POST else None
        form = exercise_form(data)
        if form.is_valid():
            arguments = {}
            for param in params:
                arguments[param] = request.POST[param]
            exercise = exercise_objects.create(**arguments)
            if type(exercise) is ReadingExercise:
                create_choices_reading(exercise, request)
            return render(request, template, {
                'form': exercise_form(),
                'role': role,
                'created': True
            })
        return HttpResponseRedirect('/thanks/')
    else:
        form = exercise_form()
        return render(request, template, {
            'form': form,
            'role': role
        })


@login_required(login_url='/website/login')
def do_exercises(request):
    return render(request, 'do_exercises.html', {
        'username': request.user.username
        })


@csrf_exempt
@login_required(login_url='/website/login')
def do_correcting_exercises(request):
    if request.method == 'POST':
        answer = request.POST['answer']
        exercise_id = request.POST['id']
        exercise = get_object_or_404(CorrectingExercise, pk=exercise_id)
        if exercise.correct_sentence == answer or\
                exercise.second_correct_sentence == answer:
            return HttpResponse('correct')
        else:
            return HttpResponse('notcorrect')
    else:
        return render(request, 'correcting-exercises.html', {
            'username': request.user.username,
            'correcting_exercises': CorrectingExercise.objects.all()
            })


@csrf_exempt
@login_required(login_url='/website/login')
def do_translating_exercises(request):
    if request.method == 'POST':
        answer = request.POST['answer']
        exercise_id = request.POST['id']
        exercise = get_object_or_404(TranslationExercise, pk=exercise_id)
        if exercise.example == answer:
            return HttpResponse('correct')
        else:
            return HttpResponse('notcorrect')
    else:
        exercises = TranslationExercise.objects.all()
        for exercise in exercises:
            shuffled = exercise.example.split()
            shuffle(shuffled)
            exercise.shuffled = shuffled
        return render(request, 'translating-exercises.html', {
            'username': request.user.username,
            'translation_exercises': exercises})


@csrf_exempt
@login_required(login_url='/website/login')
def do_reading_exercises(request):
    if request.method == 'POST':
        choice_id = request.POST['id']
        choice = get_object_or_404(Choice, pk=choice_id)
        if choice.is_correct:
            return HttpResponse('correct')
        else:
            return HttpResponse('notcorrect')
    else:
        exercises = ReadingExercise.objects.all()
        for exercise in exercises:
            exercise.choices = Choice.objects.filter(exercise=exercise)
        return render(request, 'reading-exercises.html', {
            'username': request.user.username,
            'reading_exercises': exercises})


@csrf_exempt
@login_required(login_url='/website/login')
def do_fill_in_exercises(request):
    if request.method == 'POST':
        answer = request.POST['answer']
        exercise_id = request.POST['id']
        exercise = get_object_or_404(FillInExercise, pk=exercise_id)
        if exercise.correct_answer == answer:
            return HttpResponse('correct')
        else:
            return HttpResponse('notcorrect')
    else:
        exercises = FillInExercise.objects.all()
        for exercise in exercises:
                choices = [
                    exercise.correct_answer,
                    exercise.wrong_answer,
                    exercise.second_wrong_answer]
                shuffle(choices)
                exercise.choices = choices
        return render(request, 'fillin-exercises.html', {
            'username': request.user.username,
            'fillin_exercises': exercises})


@csrf_exempt
@login_required(login_url='/website/login')
def do_ordering_exercises(request):
    if request.method == 'POST':
        first = request.POST['first']
        second = request.POST['second']
        third = request.POST['third']
        fourt = request.POST['fourt']
        exercise_id = request.POST['id']
        exercise = get_object_or_404(OrderingExercise, pk=exercise_id)
        if exercise.first_match == first and\
                exercise.second_match == second and\
                exercise.third_match == third and\
                exercise.fourt_match == fourt:
            return HttpResponse('correct')
        else:
            return HttpResponse('notcorrect')
    else:
        exercises = OrderingExercise.objects.all()
        for exercise in exercises:
                options = [
                    exercise.first_match,
                    exercise.second_match,
                    exercise.third_match,
                    exercise.fourt_match]
                shuffle(options)
                exercise.options = options
        return render(request, 'ordering-exercises.html', {
            'username': request.user.username,
            'exercises': exercises})
