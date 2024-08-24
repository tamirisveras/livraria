import imghdr
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from livraria.forms import LivroForm
from livraria.models import Livro
from django.contrib import messages
from django.contrib.auth.models import User

def deletar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    livro.delete()
    return redirect('listar_livros')

def buscar_livro(request):
    infor = request.POST.get('infor', '').strip()
    livros = Livro.objects.filter(nome__icontains=infor) if infor else []
    return render(request, 'livraria/pages/listar_livros.html', {'livros': livros})

def editar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    if request.method == "POST":
        form = LivroForm(request.POST, request.FILES, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('detalhar_livro', id=livro.id)
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livraria/pages/editar_livro.html', {'form': form})

def cadastrar_livro(request):
    if request.method == "POST":
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            livro = form.save(commit=False)
            imagem = request.FILES.get('imagem')
            if imagem and imghdr.what(imagem) in ['png', 'jpeg']:
                livro.save()
                return redirect('detalhar_livro', id=livro.id)
            else:
                messages.error(request, "Formato de imagem inválido. Apenas PNG e JPEG são aceitos.")
    else:
        form = LivroForm()
    return render(request, 'livraria/pages/editar_livro.html', {'form': form})

def detalhar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    return render(request, 'livraria/pages/detalhar_livro.html', {'livro': livro})

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livraria/pages/listar_livros.html', {'livros': livros})

def page_login(request):
    return render(request, 'livraria/pages/login.html')

def cadastro(request):
    return render(request, 'livraria/pages/cadastro.html')

def logout_usuario(request):
    logout(request)
    return redirect('page_login')

def cadastrar_usuario(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe. Tente outro.')
            return render(request, 'livraria/pages/cadastro.html')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('page_login')
    return render(request, 'livraria/pages/cadastro.html')

def autenticar_usuario(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('listar_livros')
        else:
            messages.error(request, 'Usuário ou senha inválidos. Tente novamente.')
    return render(request, 'livraria/pages/login.html')