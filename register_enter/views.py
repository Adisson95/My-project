from django.shortcuts import render
from django.http import HttpResponse

def enters(request):
    return render(request, 'register_enter/index.html') 