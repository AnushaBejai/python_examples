from question import question
question_prompts = [
    'what colour are apples?\n(a) red/green\n(b) purple\n(c) orange\n\n',
    'what colour are bananas?\n(a) teal\n(b) magenta\n(c) yellow\n\n',
    'what colour are grapes?\n(a) yellow\n(b) red\n(c) blue\n\n',
    ]
questions=[
question(question_prompts[0],'a'),
question(question_prompts[1],'c'),
question(question_prompts[2],'b'),

]
def run_test(questions):
    score=0
    for question in questions:
        answer = input(question.prompt)
        if answer== question.answer:
             score+=1
    print('you got' + str(score)+ '/'+str(len(questions))+'correct')
run_test(questions)
