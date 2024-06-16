import random

operators=["+","-","*","/"]
min_value=1
max_value=12

left=random.randint(min_value,max_value)
right=random.randint(min_value,max_value)
oper=random.choice(operators)

question=f'{left} {oper} {right}'
que=question
answer=eval(question)