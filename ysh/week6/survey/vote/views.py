from django.shortcuts import render
from django.shortcuts import redirect  
from vote.models import Survey, Answer

def home(request):
    survey_list = Survey.objects.all()
    return render(request, "index.html",{"survey_list" : survey_list})


def new(request):
    return render(request, "new.html")

def create(request):
    if (request.method == "POST"):
        survey = Survey(question = request.POST["title"], opt1= request.POST["ans1"], opt2 = request.POST["ans2"], opt3 = request.POST["ans3"], opt4=request.POST["ans4"])
        survey.save()
        return redirect('home')

def save(request, Id):
    try:
        if (request.method == "POST"):
            ans = request.POST[str(Id)]
            survey = Survey.objects.get(id=Id)
            answer = Answer(question =survey, ans=ans)
            answer.save()
            return render(request, "success.html")
    except:
        return redirect('home')

    
def result(request, Id):
    survey = Survey.objects.get(id=Id)
    answer_list = []
    answers = survey.answer_set.all()
    
    answer_list.append(answers.filter(ans = survey.opt1).count())
    answer_list.append(answers.filter(ans = survey.opt2).count())
    answer_list.append(answers.filter(ans = survey.opt3).count())
    answer_list.append(answers.filter(ans = survey.opt4).count())

    return render(request, "result.html", {"survey":survey, "answer_list" : answer_list})
    
    