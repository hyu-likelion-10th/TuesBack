from django.shortcuts import render, redirect
from .models import Survey, Answer
from .forms import SurveyForm

def main(request):
    survey_list = Survey.objects.filter().order_by('survey_idx')
    return render(request, 'main.html', {'survey_list':survey_list})

def save(request):
    survey_idx = request.POST['survey_idx']
    ans = Answer(survey_idx=int(request.POST['survey_idx']), num=request.POST['num'])
    ans.save()
    return render(request, 'complete.html',{'survey_idx':survey_idx})

def result(request, survey_idx):
    answer = Survey.objects.filter(survey_idx=survey_idx)[0]
    a1 = Answer.objects.filter(survey_idx=survey_idx, num=1).count()
    a2 = Answer.objects.filter(survey_idx=survey_idx, num=2).count()
    a3 = Answer.objects.filter(survey_idx=survey_idx, num=3).count()
    a4 = Answer.objects.filter(survey_idx=survey_idx, num=4).count()
    return render(request, 'result.html', {'answer':answer, 'a1':a1, 'a2':a2, 'a3':a3, 'a4':a4})
    #딕셔너리로 받아오면 훨씬 간단하다!!
    
def new(request):
    form = SurveyForm()
    return render(request, 'new.html', {'form':form})

def create(request):
    form = SurveyForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('main')