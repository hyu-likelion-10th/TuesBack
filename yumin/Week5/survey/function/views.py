from django.shortcuts import render
from function.models import Survey, Answer

# Create your views here.

def show_question(request):
    surveys = Survey.objects.all()
    return render(request, 'function/index.html', {'surveys': surveys})

def save_survey(request):
    answer = Answer(choice=request.POST["choice"])
    answer.save()
    return render(request, 'function/complete.html')

def show_result(request):
    results = Answer.objects.all()
    answers = [result.choice for result in results]
    counts = {}
    for answer in answers:
        try:
            counts[answer] += 1
        except:
            counts[answer] = 1
    print(counts)
    return render(request, 'function/result.html', {'counts': counts.items()})