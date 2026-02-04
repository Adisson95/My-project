from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm
from .forms import EnterForm

date = {}
counter = 1
register = False
enter = False

def index(request):
    return render(request, 'register_enter/index.html') 


def enter_view(request):
    if request.method == 'POST':
        form = EnterForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            if register == True:
                if enter == False:
                    if date.get('ide') == counter and date.get('password') == name and  date.get('email') == email: 
                        enter = True 
                        return render(request, 'register_enter/index.html')       
                else:
                    return render(request, 'register_enter/index.html')       
    else:
        form = EnterForm()

    return render(request, 'register_enter/enter_view.html', context={"form": form})

def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)

        if form.is_valid():
            global register
            global counter
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            if register == False:
                date['ide'] = counter
                date['password'] = name
                date['email'] = email
                date['age'] = age
                counter += 1
                register = True
                return render(request, 'register_enter/enter_view.html', context={"form": form})
            else:
                return render(request, 'register_enter/index.html') 
    else:
        form = MyForm()

    return render(request, 'register_enter/my_form_view.html', context={"form": form})
