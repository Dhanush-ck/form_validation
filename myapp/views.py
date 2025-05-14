from django.shortcuts import render, HttpResponse
from . forms import RegistrationForm

# Create your views here.

def home(request):
    return render(request, "index.html", {'form_page': form_page})

def form_page(request):
    form = RegistrationForm()
    return render(request, "form.html", {'form': form})