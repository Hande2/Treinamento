from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View


def home(request):
    return render(request, 'home.html')


def my_logout(request):
    logout(request)
    return redirect('home')

class HomePageView(TemplateView):
    template_name = 'home2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['minha_variavel'] = 'Ola, bem vindo ao curso avancado de Django'
        return context

class MyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home3.html')