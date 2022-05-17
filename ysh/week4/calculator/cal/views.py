from django.shortcuts import render

# Create your views here.

def home(request):
      if request.method == "POST":
            expression = request.POST.get('expression')
            val = eval(expression)
            return render(request, 'calculator.html', {'val':val})
            
      else:
            return render(request, 'home.html')

