from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET, require_POST
from .models import Student

# Create your views here.
@require_GET
def index(request):
    return render(request, 'classroom/index.html')

@require_GET
def list(request):
    students = Student.objects.all()
    return render(request, 'classroom/list.html', {
        'students':students
    })

@require_GET
def detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'classroom/detail.html', {
        'student':student
    })

@require_GET
def new(request):
    return render(request, 'classroom/new.html')

@require_POST
def create(request):
    s = Student()
    s.name = request.POST.get('name')
    s.age = request.POST.get('age')
    s.major = request.POST.get('major')
    s.save()
    return redirect('classroom:detail', s.id)

@require_GET
def edit(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'classroom/edit.html', {
        'student':student
    })

@require_POST
def update(request, id):
    s = get_object_or_404(Student, id=id)
    s.age = request.POST.get('age')
    s.major = request.POST.get('major')
    s.save()
    return redirect('classroom:detail', s.id)

@require_POST
def delete(request, id):
    s = get_object_or_404(Student, id=id)
    s.delete()
    return redirect('classroom:list')