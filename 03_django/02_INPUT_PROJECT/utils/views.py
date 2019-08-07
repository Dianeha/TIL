from django.shortcuts import render, redirect
from art import *
from datetime import datetime, date, time


def index(request):
    return render(request, 'utils/index.html')


def art(request):
    fonts = ['alpha', 'alligator2', 'advenger', '6x10', '4max']
    return render(request, 'utils/art.html', {
        'fonts': fonts
    })


def output(request):
    user_input = request.GET.get('user-input')
    user_font = request.GET.get('user-font')  # HTML 에서 name으로 value 가져오기

    if user_input:
        result = text2art(user_input, font=user_font)
        return render(request, 'utils/output.html', {
                'result': result
        })
    else:
        return redirect('/utils/art/')


def throw(request):
    return render(request, 'utils/throw.html')


def catch(request):
    s = request.GET.get('from')
    e = request.GET.get('event-date')
    eventname = request.GET.get('eventname')

    start = datetime.strptime(s, '%Y-%m-%d')
    end = datetime.strptime(e, '%Y-%m-%d')
    date = (end-start).days
    return render(request, 'utils/catch.html', {
        'date': date,
        'eventname': eventname,
    })
