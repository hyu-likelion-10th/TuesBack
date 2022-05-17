from django.shortcuts import render

def home(request):
      if request.method == "POST":
            sentence = request.POST.get('sentence')
            count, dic = word_count(sentence)
            return render(request, 'count.html', {"sentence" : sentence, "count" : count, "dictionary" : dic })
      else:
            return render(request, 'index.html')


def about(request):
      return render(request, 'about.html')

def word_count(string):
      temp = string.split(" ")
      cnt = len(temp)
      new = dict()
      for i in temp:
            if i in new:
                  new[i] += 1
            else:
                  new[i] = 1
      
      return cnt, new