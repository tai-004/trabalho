
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from pessoas.form import PessoaForm
from django.views.generic import TemplateView

from .models import Pessoa



def template(request):
    
    return render(request, 'index.html', {})

#método para listar as pessoas
@login_required
def index(request):
    pessoas = Pessoa.objects.all()
    context = {
        'pessoas': pessoas
    }
    
    return render(request, 'pessoas/index.html', context)

#método para detalhar pessoas
@login_required
def detail(request, pessoa_id):
    pessoa = Pessoa.objects.get(pk=pessoa_id)
    context = {
        'pessoa': pessoa
    }
    
    return render(request, 'pessoas/detail.html', context)

@login_required
def excluir(request, pessoa_id):
    
    Pessoa.objects.get(pk=pessoa_id).delete()
    
    return HttpResponseRedirect("/pessoas")

#método para criar uma nova pessoa
@login_required
def criar(request):
    
    if request.method == "POST":
        
        form = PessoaForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect("/pessoas")
    else:    
        form = PessoaForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'pessoas/formCriar.html', context)

#método para editar um registro de pessoa
@login_required
def editar(request, pessoa_id):
    pessoa = Pessoa.objects.get(pk=pessoa_id)
    
    if request.method == "POST":
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/pessoas")
    else:    
        form = PessoaForm(instance=pessoa)
    
    context = {
        'form': form,
        'pessoa_id': pessoa_id
    }
    
    return render(request, 'pessoas/formEdit.html', context)
    
    