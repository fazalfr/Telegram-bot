# bot/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import JokeCall

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def joke(request, category):
    joke_calls = JokeCall.objects.filter(user=request.user).first()
    if joke_calls is None:
        joke_calls = JokeCall.objects.create(user=request.user)

    if category == 'stupid':
        joke_calls.call_count += 1
    elif category == 'fat':
        joke_calls.call_count_fat += 1
    elif category == 'dumb':
        joke_calls.call_count_dumb += 1
    joke_calls.save()

    if category not in ['stupid', 'fat', 'dumb']:
        return redirect('home')

    jokes = {
        'stupid': 'Why did the chicken cross the road? To get to the other side!',
        'fat': 'Why did the tomato turn red? Because it saw the salad dressing!',
        'dumb': 'Why couldn\'t the bicycle stand up by itself? Because it was two-tired!',
    }
    joke_text
