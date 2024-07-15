from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Object
from django.shortcuts import redirect
from django.http import HttpResponse

from django.shortcuts import render


# Create your views here.

def index(request):
    name = Object.objects.all()
    date = Object.objects.all()
    specifications = Object.objects.all()
    historik = Object.objects.all()
    avariem_situation = Object.objects.all()
    return render(request, 'index.html',
                  {'name': name, 'date': date, 'specifications': specifications, 'historik': historik,
                   'avariem_situation': avariem_situation})


def documentation(request):
    return render(request, 'documentation.html')


def DC_3(request):
    return render(request, 'DC_3')


def DC_6(request):
    return render(request, 'DC_6')


def Catalina(request):
    return render(request, 'Catalina')


def Junkers_87_Stuka(request):
    return render(request, 'Junkers_87_Stuka')


class MyDetailView(DetailView):
    model = Object
    template_name = 'detail.html'
    template_nama = 'detail.html'
    context_object_name = 'test'
