from django.shortcuts import render
from django.http import HttpResponse
import random

score=0

def math(request):
    global score
    operators=["+","-","*",]
    min_value=1
    max_value=12

    left=random.randint(min_value,max_value)
    right=random.randint(min_value,max_value)
    oper=random.choice(operators)

    question=f'{left} {oper} {right}'
    answer=eval(question)

    ans=request.POST.get('answ')
    user_answer = request.POST.get('sol')

    if (user_answer == ans and user_answer!=None and ans!=None):
        expre='Correct-'
        score += 1
    elif(user_answer==None and ans==None):
        score
        expre=''
    else:
        expre='wrong-'
        score

    return render(request, 'main/home.html', {'que': question , 'score': score, 'prev_ans': answer,'exp':expre})



