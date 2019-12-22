from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404


def main(request):
    context = {
        'title': 'Login'
    }
    return render(request, 'mainapp/index.html', context=context)

def registration(request):
    context = {
        'title': 'Registration'
    }
    return render(request, 'mainapp/registration.html', context=context)




