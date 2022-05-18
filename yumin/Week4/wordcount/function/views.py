from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'function/index.html')

def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()
    word_dictionary = {}
    for word in word_list:
        try:
            word_dictionary[word] += 1
        except:
            word_dictionary[word] = 1
    return render(request, 'function/count.html', {'fulltext': full_text, 'count': len(word_list), 'words': word_dictionary.items()})

def about(request):
    return render(request, 'function/about.html')
