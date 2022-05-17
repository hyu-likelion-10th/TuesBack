from django.shortcuts import render

# Create your views here.
def calculator(request):
    in_expr = request.GET['expression']
    result = eval(in_expr)
    return render(request, 'calculator.html', {'result':result})

def main(request):
    return render(request, 'main.html')