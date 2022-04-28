from django.shortcuts import render, redirect, get_object_or_404
from .models import Question

def index(request):
    questions = Question.objects.all()
    context = {'questions': questions,}
    return render(request,'myapp/index.html', context)

def create(request):
    return render(request, 'myapp/create.html')

def insert(request):
    text = request.POST.get('text')
    question = Question(text=text)
    question.save()
    return redirect('myapp:index')

def edit(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'myapp/edit.html', context)

def update(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.text = request.POST.get('text')
    question.save()
    return redirect('myapp:index')

def delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('myapp:index')