from django.shortcuts import redirect, render
from vote.models import Survey, Answer
1,2,3,29
# Create your views here.
def home(request):
    if (request.method=="POST"):
            # print(request.POST)
            for key, value in request.POST.items():
              if key == "csrfmiddlewaretoken":
                continue
              survey = Survey.objects.get(ans=value)
              answer = Answer(response = survey)
              answer.save()
            return render(request, "finish.html")
    else:
      question_option = []
      for question in Survey.objects.all().values("question").distinct():
            q = question["question"]
            question_option.append({"question" : q, "option" : Survey.objects.filter(question=q) })
      # print(question_option)
    #   print(question_option) #[{'question': '내 나이?', 'option': <QuerySet [<Survey: 내 나이? - 1>, <Survey: 내 나이? - 2>, <Survey: 내 나이? - 3>]>}]
      return render(request, "survey.html", {"question_option_list" : question_option})


def result(request):
    question_option = []
    for question in Survey.objects.all().values("question").distinct():
        q = question["question"]
        question_option.append({"question" : q, "option" : Survey.objects.filter(question=q) })
      
    return render(request, "result.html", {"question_option_list" : question_option})


def question(request):
  if (request.method == "POST"):
    question = request.POST["title"]
    option = request.POST["option"]
    
    survey = Survey(question=question, ans=option)
    survey.save()
    return redirect('home')
  return render(request, "addquestion.html")

def add(request, question):
  if (request.method == "POST"):
    option = request.POST["option"]
    question = Survey.objects.filter(question__contains = question).values("question").distinct()[0]["question"]
    survey = Survey(question=question, ans=option)
    survey.save()
    return redirect("home")
  return render(request, 'addoption.html')

