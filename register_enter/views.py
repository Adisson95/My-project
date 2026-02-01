from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm
from .forms import EnterForm


def index(request):
    return render(request, 'register_enter/index.html') 

def enter_view(request):
    if request.method == 'POST':
        form = EnterForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']

            message = 'Успешный вход!'
            return HttpResponse(message)
    else:
        form = EnterForm()

    return render(request, 'register_enter/enter_view.html', context={"form": form})

def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']

            message = f'привет {name} валидация прошла успешно!'
            return HttpResponse(message)
    else:
        form = MyForm()

    return render(request, 'register_enter/my_form_view.html', context={"form": form})
