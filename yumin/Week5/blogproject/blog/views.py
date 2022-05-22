from django.shortcuts import render, redirect, get_object_or_404

from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommentModelForm

def home(request):
    posts = Blog.objects.filter().order_by('-date')
    return render(request, 'blog/index.html', {'posts': posts})

def new(request):
    return render(request, 'blog/new.html')

def create(request):
    if request.method == 'POST':
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

def formcreate(request):
    # GET: Give HTML
    # POST: Save the input content
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            #post.date = timezone.now()
            post.save()
            return redirect('home')
    else: # GET
        form = BlogForm()
    return render(request, 'blog/form_create.html', {'form': form})

def modelformcreate(request):
    # GET: Give HTML
    # POST: Save the input content
    if request.method == 'POST' or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else: # GET
        form = BlogModelForm()
    return render(request, 'blog/form_create.html', {'form': form})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    comment_form = CommentModelForm()

    return render(request, 'blog/detail.html', {'blog_detail': blog_detail, 'comment_form': comment_form})

def create_comment(request, blog_id):
    filled_form = CommentModelForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Blog, pk=blog_id)
        finished_form.save()
    return redirect('detail', blog_id)