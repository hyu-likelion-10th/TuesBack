from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    in_text = request.GET['sentence']
    word_list = in_text.split()
    dic = {}
    for word in word_list:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return render(request, 'count.html', {'text':in_text, 'count':len(word_list),'dic':dic.items()})