from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def competences(request):
    return render(request, 'competences.html')

def projets(request):
    return render(request,'projets.html')

def contact(request):
    return render(request,'contact.html')


# Create your views here.
