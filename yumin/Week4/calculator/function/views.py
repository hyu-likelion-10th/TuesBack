from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'function/index.html')

def calculator(request):
    eq = request.GET['equation']
    return render(request, 'function/calculator.html', {'result': eval(eq)})

