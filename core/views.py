from django.shortcuts import render

# Create your views here.
# def home(request):
#  return render(request, 'core/home.html)

def home(request):
    contexto={"nombre":"Del Perrito"}
    return render(request, 'core/home.html', contexto)