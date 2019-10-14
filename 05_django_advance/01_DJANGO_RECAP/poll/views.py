from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Question, Choice
from .forms import ChoiceModelForm

# Create your views here.
def poll_result(request):
    question = Question.objects.get(id=1)
    form = ChoiceModelForm()
    choices = question.choice_set.all()
    return render(request, 'poll/question_detail.html', {
        'question': question,
        'form': form,
        'choices': choices,
    })

def update_poll(request):
    if request.method == "POST":
        res = request.POST.get('content')        
        c = Choice.objects.get(content=res)
        c.votes += 1
        c.save()       

    return redirect('poll:poll_result')