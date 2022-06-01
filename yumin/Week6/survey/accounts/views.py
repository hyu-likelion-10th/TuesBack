from django.shortcuts import render, redirect
from .models import Survey, Answer
from .forms import SurveyForm
"""
main : 설문조사를 목록 형식으로 보여줌 (여러개 표시)
save : 각 설문조사에 대해 응답하고 완료창으로 이동
result : 각 설문조사에 대해 응답결과 보여줌
new : 새로운 설문조사 작성 화면 보여줌
create : 새로운 설문조사 만들기(POST), main으로 돌아감
"""

# Create your views here.
def main(request):
    surveys = Survey.objects.all()
    return render(request, 'accounts/main.html', {'surveys': surveys})

def save(request):
    survey_idx = request.POST["survey_idx"]
    answer = Answer(survey_idx=survey_idx, ans=request.POST["num"])
    answer.save()
    return render(request, "accounts/complete.html")

def result(request, question_id):
    examples = Survey.objects.filter(survey_idx=question_id).values('ans1', 'ans2', 'ans3', 'ans4')[0]
    answers = Answer.objects.filter(survey_idx=question_id).values('ans')
    result = {examples['ans1']: 0, examples['ans2']: 0, examples['ans3']: 0, examples['ans4']: 0}
    for answer in answers:
        print('answersin:', answer['ans'])
        result[answer['ans']] += 1
    return render(request, "accounts/result.html", {'result': result.items()})

def new(request):
    form = SurveyForm()
    return render(request, 'accounts/new.html', {'form': form})

def create(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = SurveyForm()
        return render(request, 'accounts/new.html', {'form': form})
