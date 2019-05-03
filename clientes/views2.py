<<<<<<< HEAD
from django.http import HttpResponse, JsonResponse
=======
from django.http import HttpResponse
>>>>>>> 57998c57ef898d8cbdbac9a5f18b40341a245d57
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Person
from produtos.models import Produto
from vendas.models import Venda
from .forms import PersonForm
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView, DeleteView

<<<<<<< HEAD

=======
>>>>>>> 57998c57ef898d8cbdbac9a5f18b40341a245d57
@login_required
def persons_list(request):
    persons = Person.objects.all()
    footer_message = "Aqui tem coragem"
    return render(
        request, 'person.html', {'persons': persons, 'footer_message': footer_message})

<<<<<<< HEAD
    # nome = request.GET.get('nome', None)
    # sobrenome = request.GET.get('sobrenome', None)
    # checkbox = request.GET.get('meu-checkbox', None)

    # if checkbox == 'on':
    # persons = Person.objects.filter(ativo=True)

    # if nome or sobrenome:
    # persons = Person.objects.filter(first_name__icontains=nome) | Person.objects.filter(last_name__icontains=sobrenome)

    # else:

    # return render(request, 'person.html', {'persons': persons, 'footer_message': footer_message})
=======

    #nome = request.GET.get('nome', None)
    #sobrenome = request.GET.get('sobrenome', None)
    #checkbox = request.GET.get('meu-checkbox', None)

    #if checkbox == 'on':
        #persons = Person.objects.filter(ativo=True)

    #if nome or sobrenome:
        #persons = Person.objects.filter(first_name__icontains=nome) | Person.objects.filter(last_name__icontains=sobrenome)

    #else:


    #return render(request, 'person.html', {'persons': persons, 'footer_message': footer_message})

>>>>>>> 57998c57ef898d8cbdbac9a5f18b40341a245d57


@login_required
def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("person_list")
    return render(request, 'person_form.html', {'form': form})

<<<<<<< HEAD

=======
>>>>>>> 57998c57ef898d8cbdbac9a5f18b40341a245d57
@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect("person_list")
    return render(request, 'person_form.html', {'form': form})

<<<<<<< HEAD

=======
>>>>>>> 57998c57ef898d8cbdbac9a5f18b40341a245d57
@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

<<<<<<< HEAD
=======

>>>>>>> 57998c57ef898d8cbdbac9a5f18b40341a245d57
    if request.method == 'POST':
        person.delete()
        return redirect("person_list")
    return render(request, "person_delete_confirma.html", {'person': person})

<<<<<<< HEAD

class PersonList(LoginRequiredMixin, ListView):
=======
class PersonList(LoginRequiredMixin ,ListView):
>>>>>>> 57998c57ef898d8cbdbac9a5f18b40341a245d57
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        primeiro_acesso = self.request.session.get('primeiro_acesso', False)

        if not primeiro_acesso:
            context['message'] = 'Seja bem vindo ao seu primeiro acesso hoje'
<<<<<<< HEAD
            self.request.session['primeiro_acesso'] = True
=======
            self.request.session ['primeiro_acesso'] = True
>>>>>>> 57998c57ef898d8cbdbac9a5f18b40341a245d57
        else:
            context['message'] = 'Você já acessou hoje'

        return context

<<<<<<< HEAD

=======
>>>>>>> 57998c57ef898d8cbdbac9a5f18b40341a245d57
class PersonDetail(LoginRequiredMixin, DetailView):
    model = Person

    def get_context_data(self, **kwargs):
<<<<<<< HEAD
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PersonCreate(LoginRequiredMixin, CreateView):
=======
        context =super().get_context_data(**kwargs)
        context ['now'] = timezone.now()
        return context

class PersonCreate (LoginRequiredMixin, CreateView):
>>>>>>> 57998c57ef898d8cbdbac9a5f18b40341a245d57
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = '/clientes/person_list'

<<<<<<< HEAD

class PersonUpdate(LoginRequiredMixin, UpdateView):
=======
class PersonUpdate (LoginRequiredMixin, UpdateView):
>>>>>>> 57998c57ef898d8cbdbac9a5f18b40341a245d57
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = '/clientes/person_list'

<<<<<<< HEAD

class PersonDetele(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
=======
class PersonDetele (LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
>>>>>>> 57998c57ef898d8cbdbac9a5f18b40341a245d57
    permission_required = ('clientes.deletar_clientes',)

    model = Person
    success_url = '/clientes/person_list'

    # def get_success_url(self):
<<<<<<< HEAD
    # return reverse_lazy('person_list_cb')

=======
       # return reverse_lazy('person_list_cb')
>>>>>>> 57998c57ef898d8cbdbac9a5f18b40341a245d57

"""ProdutoBulk(View):
    def get(self, request):
       produtos = ['Banana', 'Maca', 'Limao', 'Laranja', 'Pera', 'Melancia']
        list_produtos = []

        for produto in produtos:
            p = Produto(descricao=produto, preco=10)
            list_produtos.append(p)

        Produto.objects.bulk_create(list_produtos)

<<<<<<< HEAD
        return HttpResponse('Funcionou')"""


=======
        return HttpResponse('Funcionou')"""
>>>>>>> 57998c57ef898d8cbdbac9a5f18b40341a245d57
