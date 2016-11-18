from django.shortcuts import render
from .models import Libro
from .forms import LibroForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
# Create your views here.
def post_list(request):
    posts = Libro.objects.all
    return render(request, 'blogbiblioteca/post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blogbiblioteca.views.post_detail', pk=post.pk)
    else:
        form = LibroForm()
    return render(request, 'blogbiblioteca/post_edit.html', {'form': form})

def post_detail (request, pk):
    post = get_object_or_404(Libro, pk=pk)
    return render(request, 'blogbiblioteca/post_detail.html', {'post': post})
def post_edit(request, pk):
    post = get_object_or_404(Libro, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blogbiblioteca.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blogbiblioteca/post_edit.html', {'form': form})
