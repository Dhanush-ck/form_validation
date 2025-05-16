from django.shortcuts import render, HttpResponse
from . forms import RegistrationForm

# Create your views here.

def home(request):
    return render(request, "index.html", {'form_page': form_page})


def form_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            return render(request, 'result.html', {
                'username': username,
                'email': email,
                'password': password,
                })
    else:
        form = RegistrationForm()
    return render(request, "form.html", {
        'form': form,
        })

def result_page(request):
    return render(request, "result.html")