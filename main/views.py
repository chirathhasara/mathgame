from django.shortcuts import render
from django.http import HttpResponse
from . import math_quiz

def math(request):

    math_quiz.que=math_quiz.question
    ans=request.POST.get('answ')
    return render(request,'main/home.html',{'que':math_quiz.que,'ans':ans,"answer":math_quiz.answer})



