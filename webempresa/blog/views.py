from django.shortcuts import render, get_object_or_404
from .models import Post, Categori
# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(request,'blog/blog.html',{'posts':posts})

def blog_category(request,category_id):
    category = get_object_or_404(Categori,id=category_id)
    posts = category.get_posts.all()
    return render(request, 'blog/blog.html', {'posts':posts})
    #return render(request, 'blog/blog_category.html',{'category':category})
