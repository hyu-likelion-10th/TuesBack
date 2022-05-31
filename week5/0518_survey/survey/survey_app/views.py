from django.shortcuts import render
from .models import Survey, Answer

def main(request):
    survey = Survey.objects.filter().order_by('survey_idx')[0]
    return render(request, 'main.html', {'survey':survey})

def save_survey(request):
    survey_idx = request.POST['survey_idx']
    ans = Answer(survey_idx=int(request.POST['survey_idx']), num=request.POST['num'])
    ans.save()
    return render(request, 'votecomplete.html',{'survey_idx':survey_idx})

def result(request, survey_idx):
    answer = Survey.objects.filter(survey_idx=survey_idx)[0]
    a1 = Answer.objects.filter(survey_idx=survey_idx, num=1).count()
    a2 = Answer.objects.filter(survey_idx=survey_idx, num=2).count()
    a3 = Answer.objects.filter(survey_idx=survey_idx, num=3).count()
    a4 = Answer.objects.filter(survey_idx=survey_idx, num=4).count()
    return render(request, 'result.html', {'answer':answer, 'a1':a1, 'a2':a2, 'a3':a3, 'a4':a4})