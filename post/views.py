from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template.defaulttags import register
from babel.dates import format_timedelta
from datetime import  timedelta
from .forms import CommentForm

@register.filter
def formatar_data(value):
    time = timedelta(seconds=value.timestamp() - value.now().timestamp())
    return format_timedelta(time, add_direction=True)

@never_cache
def login_user(request):
    if request.user.is_authenticated:
        return redirect('/post/')
    return render(request, 'post/login.html')

def login_auth(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/post/')
        else:
             messages.error(request, 'Usuário ou senha inválidos')
        
    return redirect('/login/')

def logout_user(request):
    logout(request)
    
    return redirect ('/post/')
@login_required(login_url='/login/')
def about(request):
    return render(request, 'post/about.html')

#Página principal
@login_required(login_url='/login/')
def home(request):
    return render(request, 'post/posts_all.html', {'posts': Blog.objects.all()})

#Ir ao form
@login_required(login_url='/login/')
def form(request):
    return render(request, 'post/post.html')

#Create
@login_required(login_url='/login/')
def postar(request):
    if request.POST:
        title = request.POST['title'].strip().upper()
        text = request.POST['text'].strip().upper()
        author = request.user
        Blog.objects.create(title=title, text=text, author=author)
        return redirect('/post/')

#Delete 
@login_required(login_url='/login/')
def delete_post(request, id_post):
    user = request.user
    post = Blog.objects.get(id=id_post)
    if (user == post.author):
        post.delete()
    return redirect('/post/')

#Load update
def edit_post(request, id_post):
    data = {'post' : Blog.objects.get(id=id_post)}
    if (request.user == data['post'].author):
        return render(request, 'post/post.html', data)
    return redirect ('/post/')

#Save update
@login_required(login_url='/login/')
def update_post(request, id_post):
    if request.POST:
        title = request.POST.get('title').strip().upper()
        text = request.POST.get('text').strip().upper()
        author = request.user
        
        Blog.objects.filter(id=id_post).update(title=title, text=text, author=author)

    return redirect('/post/')

#Visualizar
@login_required(login_url='/login/')
def view_post(request, id_post):
    post = Blog.objects.get(id=id_post)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('/post/',id_post)
    else:
        form = CommentForm

    data = {
        'post': post,
        'form': form
    }

    data['form'].author = request.user

    return render(request, 'post/view_post.html', data)


