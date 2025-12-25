from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def experience(request):
    return render(request, "core/experience.html")

def projects(request):
    return render(request, "core/projects.html")

def contact(request):
    return render(request, "core/contact.html")