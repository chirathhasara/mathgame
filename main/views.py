from django.shortcuts import render
from django.http import HttpResponse
import random


def math(request):
    while True:
        operators=["+","-","*","/"]
        min_value=1
        max_value=12

        left=random.randint(min_value,max_value)
        right=random.randint(min_value,max_value)
        oper=random.choice(operators)

        question=f'{left} {oper} {right}'
        que=question
        ans=request.POST.get('answ')
       
        return render(request,'main/home.html',{'que':que,'ans':ans,"answer":eval(question)})



