from django.shortcuts import render
from django.http import HttpResponse
import random
import time


    
  

def math(request):

    operators=["+","-","*","/"]
    min_value=1
    max_value=12

    left=random.randint(min_value,max_value)
    right=random.randint(min_value,max_value)
    oper=random.choice(operators)

    question=f'{left} {oper} {right}'
    score=0
    que=question
    answer=eval(question)
    while True:
        ans=request.POST.get('answ')
        if ans==answer:
            score=score+1
        return render(request,'main/home.html',{'answer':answer,'que':que,'score':score,'ans':ans})



