from django.shortcuts import render, redirect
from .forms import *
from .models import *

def index(request):
    newsPosts = Post.objects.all()
    return render(request, 'news/index.html', context={'newsPosts': newsPosts})


def createNews(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        urladdress = request.POST.get('urladdress')
        isPublic = request.POST.get('isPublic')
        if isPublic == 'on':
            isPublic = True
        else:
            isPublic = False
        category = request.POST.get('category')

        
        p, _ = Post.objects.get_or_create(
            title=title, 
            content=content, 
            urladdress=urladdress, 
            isPublic=isPublic, 
            category=category,
        )
        return redirect('home')
    else:
        form = CreatePost()
        return render(request, 'news/create.html', context={'form': form})
