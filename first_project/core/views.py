from django.shortcuts import render, redirect
from django.urls import reverse
from core.forms import PostForm, UpdatePostForm
from .models import Post, Category
from django.contrib import messages

# Create your views here.

def home(request):
    posts = Post.objects.all()
    cats = Category.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.save()
            messages.success(request, 'Post created successfully')
            return redirect('home')
        else:
            messages.error(request, 'Failed to create post')
            return redirect('home') 
    else:
        form = PostForm()
    context = {
        'cats':cats,
        'form':form,
        'posts':posts
        }
    return render(request, 'core/home.html', context)
def update_post(request, pk):
    post = Post.objects.get(pk=pk)  
    if request.method == 'POST':    
        form = UpdatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully')
            return redirect(reverse('post-detail', args=[post.pk]))
        else:
            messages.error(request, 'Failed to update post')
            return redirect(reverse('post-detail', args=[post.pk])) 
    form = UpdatePostForm(instance=post)
    context = {
        'form': form,
        'post': post,
        'cats': Category.objects.all()
    }
    return render(request, 'core/post.html', context)
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    messages.warning(request, 'post deleted successfully')
    return redirect('home')

def post(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post':post}
    return render(request, 'core/post.html', context)


