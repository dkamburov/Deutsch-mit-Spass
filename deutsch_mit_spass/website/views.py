from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from website.forms import LoginForm, RegisterForm, CorrectingExerciseForm
from website.models import CorrectingExercise
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


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
    role = request.user.ROLE_CHOISES[request.user.role][1]
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
            registered = True
    return render(request, 'register.html', locals())


def exercises_view(request):
    role = request.user.ROLE_CHOISES[request.user.role][1]
    return render(request, 'exercises.html', {
        'username': request.user.username,
        'role': role
    })


def correction_view(request):
    role = request.user.ROLE_CHOISES[request.user.role][1]
    if request.method == 'POST':
        data = request.POST if request.POST else None
        form = CorrectingExerciseForm(data)
        if form.is_valid():
            correct_sentence = request.POST['correct_sentence']
            second_correct_sentence = request.POST['second_correct_sentence']
            wrong_sentence = request.POST['wrong_sentence']
            CorrectingExercise.objects.create(
                correct_sentence=correct_sentence,
                second_correct_sentence=second_correct_sentence,
                wrong_sentence=wrong_sentence)
            return render(request, 'correction.html', {
                'form': CorrectingExerciseForm(),
                'role': role,
                'created': True
            })
        return HttpResponseRedirect('/thanks/')
    else:
        form = CorrectingExerciseForm()
        return render(request, 'correction.html', {
            'form': form,
            'role': role
        })


@csrf_exempt
def do_exercises_view(request):
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
        return render(request, 'do_exercises.html', {
            'username': request.user.username,
            'correcting_exercises': CorrectingExercise.objects.all()
            })
